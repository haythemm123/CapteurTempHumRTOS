import 'dart:convert';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';
import 'package:http/http.dart' as http;
import 'package:fl_chart/fl_chart.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.blue, useMaterial3: true),
      home: const SensorDashboard(),
    );
  }
}

class SensorDashboard extends StatefulWidget {
  const SensorDashboard({super.key});
  @override
  State<SensorDashboard> createState() => _SensorDashboardState();
}

class _SensorDashboardState extends State<SensorDashboard> {
  // 10.0.2.2 is the bridge from the Android Emulator to your PC Localhost
  final String mqttBroker = "10.0.2.2"; 
  final String apiBaseUrl = "http://10.0.2.2:5000/history";
  final String topic = "pfe/sensor/data";
  final String clientIdentifier = "pfe_mobile_${DateTime.now().millisecondsSinceEpoch}";

  late MqttServerClient client;
  double temperature = 0.0;
  double humidity = 0.0;
  bool isConnected = false;
  List<dynamic> historyData = [];
  Timer? refreshTimer;

  @override
  void initState() {
    super.initState();
    setupMqtt();
    fetchHistory();
    // Auto-refresh the database data every 10 seconds
    refreshTimer = Timer.periodic(const Duration(seconds: 10), (timer) {
      if (mounted) fetchHistory();
    });
  }

  @override
  void dispose() {
    refreshTimer?.cancel();
    super.dispose();
  }

  Future<void> fetchHistory() async {
    try {
      final response = await http.get(Uri.parse(apiBaseUrl));
      if (response.statusCode == 200) {
        setState(() => historyData = jsonDecode(response.body));
      }
    } catch (e) {
      print("❌ API Error: $e");
    }
  }

  Future<void> setupMqtt() async {
    client = MqttServerClient(mqttBroker, clientIdentifier);
    client.port = 1883;
    client.keepAlivePeriod = 20;
    client.onDisconnected = onDisconnected;
    client.onConnected = onConnected;

    final connMessage = MqttConnectMessage()
        .withClientIdentifier(clientIdentifier)
        .startClean()
        .withWillQos(MqttQos.atLeastOnce);
    client.connectionMessage = connMessage;

    try {
      await client.connect();
    } catch (e) {
      client.disconnect();
      return;
    }

    if (client.connectionStatus!.state == MqttConnectionState.connected) {
      setState(() => isConnected = true);
      client.subscribe(topic, MqttQos.atMostOnce);

      client.updates!.listen((List<MqttReceivedMessage<MqttMessage>> c) {
        final MqttPublishMessage recMess = c[0].payload as MqttPublishMessage;
        final String pt = MqttPublishPayload.bytesToStringAsString(recMess.payload.message);
        
        try {
          final Map<String, dynamic> data = jsonDecode(pt);
          setState(() {
            temperature = data['temperature']?.toDouble() ?? 0.0;
            humidity = data['humidity']?.toDouble() ?? 0.0;
          });
        } catch (e) {
          print("❌ MQTT JSON Error: $e");
        }
      });
    }
  }

  void onConnected() => setState(() => isConnected = true);
  void onDisconnected() => setState(() => isConnected = false);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("IoT Sensor Dashboard"),
        actions: [IconButton(onPressed: fetchHistory, icon: const Icon(Icons.refresh))],
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              Icon(
                isConnected ? Icons.cloud_done : Icons.cloud_off,
                color: isConnected ? Colors.green : Colors.red,
                size: 50,
              ),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  _buildSensorCard("Temp", "$temperature°C", Colors.orange),
                  _buildSensorCard("Hum", "$humidity%", Colors.blue),
                ],
              ),
              const SizedBox(height: 30),
              const Text("Temperature History", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.orange)),
              const SizedBox(height: 10),
              _buildChart(isTemp: true, color: Colors.orange),
              const SizedBox(height: 30),
              const Text("Humidity History", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.blue)),
              const SizedBox(height: 10),
              _buildChart(isTemp: false, color: Colors.blue),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildChart({required bool isTemp, required Color color}) {
    if (historyData.isEmpty) {
      return const SizedBox(height: 180, child: Center(child: Text("Loading DB Data...")));
    }

    return Container(
      height: 220,
      padding: const EdgeInsets.only(right: 20, top: 10),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(15),
        boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 4)],
      ),
      child: LineChart(
        LineChartData(
          gridData: const FlGridData(show: true, drawVerticalLine: false),
          titlesData: const FlTitlesData(
            rightTitles: AxisTitles(sideTitles: SideTitles(showTitles: false)),
            topTitles: AxisTitles(sideTitles: SideTitles(showTitles: false)),
          ),
          borderData: FlBorderData(show: false),
          lineBarsData: [
            LineChartBarData(
              spots: historyData.asMap().entries.map((e) {
                // Mapping keys from your pfe_data.db 
                double val = isTemp ? e.value['temp'].toDouble() : e.value['hum'].toDouble();
                return FlSpot(e.key.toDouble(), val);
              }).toList(),
              isCurved: true,
              barWidth: 4,
              dotData: const FlDotData(show: false),
              // Use gradient for modern fl_chart compatibility
              gradient: LinearGradient(colors: [color, color.withOpacity(0.7)]),
              // FIXED: Changed belowArea to belowBarData
              belowBarData: BarAreaData(
                show: true,
                gradient: LinearGradient(
                  colors: [color.withOpacity(0.3), color.withOpacity(0.0)],
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSensorCard(String label, String value, Color color) {
    return Container(
      width: 150,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(15),
        border: Border.all(color: color, width: 2),
      ),
      child: Column(
        children: [
          Text(label),
          Text(value, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: color)),
        ],
      ),
    );
  }
}