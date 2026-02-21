import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

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
  // Use the full WSS scheme here to satisfy the library requirements
  final String broker = "192.168.49.1";
  final String topic = "pfe/sensor/data";
  final String clientIdentifier =
      "pfe_mobile_${DateTime.now().millisecondsSinceEpoch}";

  late MqttServerClient client;
  double temperature = 0.0;
  double humidity = 0.0;
  bool isConnected = false;

  @override
  void initState() {
    super.initState();
    setupMqtt();
  }

  Future<void> setupMqtt() async {
    // Use MqttServerClient for standard TCP connection
    client = MqttServerClient(broker, clientIdentifier);
    client.port = 1883; // Standard Mosquitto Port
    client.keepAlivePeriod = 20;
    client.onDisconnected = onDisconnected;
    client.onConnected = onConnected;
    client.logging(on: true);

    final connMessage = MqttConnectMessage()
        .withClientIdentifier(clientIdentifier)
        .startClean()
        .withWillQos(MqttQos.atLeastOnce);
    client.connectionMessage = connMessage;

    try {
      print('🚀 MQTT: Connecting to Local Mosquitto (10.0.2.2)...');
      await client.connect();
    } catch (e) {
      print('❌ MQTT Exception: $e');
      client.disconnect();
      return;
    }

    if (client.connectionStatus!.state == MqttConnectionState.connected) {
      setState(() => isConnected = true);
      client.subscribe(topic, MqttQos.atMostOnce);
      print('✅ MQTT: Connected to Local Broker!');

      client.updates!.listen((List<MqttReceivedMessage<MqttMessage>> c) {
        final MqttPublishMessage recMess = c[0].payload as MqttPublishMessage;
        final String pt = MqttPublishPayload.bytesToStringAsString(
          recMess.payload.message,
        );

        print('📥 Local Data: $pt');

        final Map<String, dynamic> data = jsonDecode(pt);
        setState(() {
          temperature = data['temperature']?.toDouble() ?? 0.0;
          humidity = data['humidity']?.toDouble() ?? 0.0;
        });
      });
    }
  }

  void onConnected() => setState(() => isConnected = true);
  void onDisconnected() => setState(() => isConnected = false);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("IoT Sensor Dashboard")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              isConnected ? Icons.cloud_done : Icons.cloud_off,
              color: isConnected ? Colors.green : Colors.red,
              size: 60,
            ),
            Text(isConnected ? "Connected to Broker" : "Disconnected"),
            const SizedBox(height: 40),
            _buildSensorCard(
              "Temperature",
              "$temperature°C",
              Icons.thermostat,
              temperature > 30.0 ? Colors.red : Colors.orange,
            ),
            const SizedBox(height: 20),
            _buildSensorCard(
              "Humidity",
              "$humidity%",
              Icons.water_drop,
              Colors.blue,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSensorCard(
    String title,
    String value,
    IconData icon,
    Color color,
  ) {
    return Container(
      width: 260,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color, width: 2),
      ),
      child: Column(
        children: [
          Icon(icon, size: 40, color: color),
          Text(
            title,
            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          Text(
            value,
            style: TextStyle(
              fontSize: 32,
              color: color,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}
