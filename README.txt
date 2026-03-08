USE [CRES_ODS]
GO
/****** Object:  Table [dbo].[ODSAccordAccouchement]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordAccouchement](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[PRST] [nvarchar](255) NULL,
	[FIL] [nvarchar](255) NULL,
	[TYPE_ACCOUCH] [nvarchar](255) NULL,
	[DATE_ACCOUCH] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordAppareillage]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordAppareillage](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[PRST] [nvarchar](255) NULL,
	[FIL] [nvarchar](255) NULL,
	[DATE_LIVRAISON] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordCardio]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordCardio](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSSE] [nvarchar](255) NULL,
	[ACT_COD_REEL] [nvarchar](255) NULL,
	[ACTE_REEL_PRATIQUE] [nvarchar](255) NULL,
	[DATE_INTERVENTION] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordCureThermale]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordCureThermale](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[PRST] [nvarchar](255) NULL,
	[FIL] [nvarchar](255) NULL,
	[DATE_PAI4EMENT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordDialyse]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordDialyse](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[PRST] [nvarchar](255) NULL,
	[FIL] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[DATE_PAI4EMENT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordGreffe]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordGreffe](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordHospitalisation]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordHospitalisation](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[DATE_HOSPITALISATION] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordMedicamentOfficinal]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordMedicamentOfficinal](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[CODE_MED] [nvarchar](255) NULL,
	[LIB_MED] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[NB_BOITES] [nvarchar](255) NULL,
	[MONTANT] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[CODE_MED_LIVRE] [nvarchar](255) NULL,
	[LIB_MED_LIVRE] [nvarchar](255) NULL,
	[QTE_LIVRE] [nvarchar](255) NULL,
	[MONTANT_MED_LIVRE] [nvarchar](255) NULL,
	[DATE_DISPENSATION] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordMedicamentSpecifique]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordMedicamentSpecifique](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[DATE_VALIDATION] [nvarchar](255) NULL,
	[CODE_MED] [nvarchar](255) NULL,
	[TYP_MED] [nvarchar](255) NULL,
	[LIB_MED] [nvarchar](255) NULL,
	[DCI] [nvarchar](255) NULL,
	[QTE] [nvarchar](255) NULL,
	[COMMISSION] [nvarchar](255) NULL,
	[POLICLINIQUE] [nvarchar](255) NULL,
	[ORGANISME_ACCORD] [nvarchar](255) NULL,
	[COD_ARTICLE_LIVRE] [nvarchar](255) NULL,
	[LIB_ARTICLE_LIVRE] [nvarchar](255) NULL,
	[TRANCH_LIV] [nvarchar](255) NULL,
	[QTE_TRANCH_LIV] [nvarchar](255) NULL,
	[NB_DUR] [nvarchar](255) NULL,
	[UNIT] [nvarchar](255) NULL,
	[DATE_LIVRAISON] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordOrthophonieOrthoptie]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordOrthophonieOrthoptie](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordRadiologie]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordRadiologie](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordRadiotherapie]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordRadiotherapie](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSAccordScintigraphie]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSAccordScintigraphie](
	[ANNE_EXERCICE] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[QUALITE] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[NOM] [nvarchar](255) NULL,
	[NAISSANCE] [nvarchar](255) NULL,
	[BR] [nvarchar](255) NULL,
	[BUREAU] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[NUM] [nvarchar](255) NULL,
	[EDITION] [nvarchar](255) NULL,
	[PRST_COD] [nvarchar](255) NULL,
	[PRESTATION] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[FORFAIT] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[CODE] [nvarchar](255) NULL,
	[CLEF] [nvarchar](255) NULL,
	[NOM_FOUR] [nvarchar](255) NULL,
	[MONTANT_FACTURE] [nvarchar](255) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[DATE_PAIEMENT] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[ExecID] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSBeneficiaire]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSBeneficiaire](
	[IU_BNF] [nvarchar](255) NULL,
	[NOM_PHON] [nvarchar](255) NULL,
	[PRE_PHON] [nvarchar](255) NULL,
	[PRE_PER_PHON] [nvarchar](255) NULL,
	[PRE_GPR_PHON] [nvarchar](255) NULL,
	[NOM_MER_PHON] [nvarchar](255) NULL,
	[PRE_MER_PHON] [nvarchar](255) NULL,
	[SEX_BNF] [nvarchar](255) NULL,
	[DAT_NAI_BNF] [nvarchar](255) NULL,
	[COD_PAY_NAI] [nvarchar](255) NULL,
	[SIT_FAM_BNF] [nvarchar](255) NULL,
	[TYP_PID_BNF] [nvarchar](255) NULL,
	[NUM_PID_BNF] [nvarchar](255) NULL,
	[COD_POS] [nvarchar](255) NULL,
	[DAT_RAT_CNSS_BNF] [nvarchar](255) NULL,
	[MAT_AFF_CNSS_BNF] [nvarchar](255) NULL,
	[COD_POS_BNF] [nvarchar](255) NULL,
	[DAT_POS_BNF] [nvarchar](255) NULL,
	[COD_LIE_PAR] [nvarchar](255) NULL,
	[IU_BNF_DRO] [nvarchar](255) NULL,
	[IU_BNF_PER] [nvarchar](255) NULL,
	[IU_BNF_MER] [nvarchar](255) NULL,
	[IU_BNF_CNJ] [nvarchar](255) NULL,
	[DAT_CRE_BNF] [nvarchar](255) NULL,
	[DAT_MOD_BNF] [nvarchar](255) NULL,
	[DAT_RAT_BNF] [nvarchar](255) NULL,
	[DAT_RAT_CNRPS_BNF] [nvarchar](255) NULL,
	[EXISTE_CNSS] [nvarchar](255) NULL,
	[EXISTE_CNRPS] [nvarchar](255) NULL,
	[EXISTE_MAS] [nvarchar](255) NULL,
	[COD_ETA] [nvarchar](255) NULL,
	[RACINE] [nvarchar](255) NULL,
	[NUM_PID_BNF_NUMBER] [nvarchar](255) NULL,
	[FLG_ANN] [nvarchar](255) NULL,
	[DAT_ANN_BNF] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSBeneficiaireCnam]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSBeneficiaireCnam](
	[BEN_DATN] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[BEN_FAM] [nvarchar](255) NULL,
	[BEN_SEXE] [nvarchar](255) NULL,
	[LOC_COD] [nvarchar](255) NULL,
	[BEN_BUR] [nvarchar](255) NULL,
	[BEN_DECES] [nvarchar](255) NULL,
	[DATE_CRE] [nvarchar](255) NULL,
	[ID_CRESS] [nvarchar](255) NULL,
	[DATE_FAM] [nvarchar](255) NULL,
	[RANG_CONJ] [nvarchar](255) NULL,
	[DATE_EFFET] [nvarchar](255) NULL,
	[BEN_SIT] [nvarchar](255) NULL,
	[DATE_BENEF_CRE] [nvarchar](255) NULL,
	[BEN_VALID] [nvarchar](255) NULL,
	[BEN_DATE_VALID] [nvarchar](255) NULL,
	[STR_COD_VALID] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSCapitalDeces]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSCapitalDeces](
	[MATRICULE] [nvarchar](255) NULL,
	[CODE_AYANT_DROIT] [nvarchar](255) NULL,
	[TYPE_AYANT_DROIT] [nvarchar](255) NULL,
	[DATE_NAISSANCE] [nvarchar](255) NULL,
	[PART] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSChefMenage]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSChefMenage](
	[id_gouv] [nvarchar](255) NULL,
	[lib_gouv] [nvarchar](255) NULL,
	[id_del] [nvarchar](255) NULL,
	[lib_del] [nvarchar](255) NULL,
	[code_postal_s] [nvarchar](255) NULL,
	[num_compte] [nvarchar](255) NULL,
	[status] [nvarchar](255) NULL,
	[id_typeidentifiant] [nvarchar](255) NULL,
	[n_cin] [nvarchar](255) NULL,
	[ident_uni] [nvarchar](255) NULL,
	[nom_dem] [nvarchar](255) NULL,
	[prenom_dem] [nvarchar](255) NULL,
	[prenom_pere] [nvarchar](255) NULL,
	[prenom_gd_pere] [nvarchar](255) NULL,
	[nom_mere] [nvarchar](255) NULL,
	[prenom_mere] [nvarchar](255) NULL,
	[sexechef] [nvarchar](255) NULL,
	[date_nais_chef] [nvarchar](255) NULL,
	[naissance_etaranger] [nvarchar](255) NULL,
	[pays] [nvarchar](255) NULL,
	[id_etat_civil] [nvarchar](255) NULL,
	[date_ouverture] [nvarchar](255) NULL,
	[date_modif] [nvarchar](255) NULL,
	[a_handicap] [nvarchar](255) NULL,
	[lib] [nvarchar](255) NULL,
	[lib_type_soin] [nvarchar](255) NULL,
	[decile] [nvarchar](255) NULL,
	[Situation] [nvarchar](255) NULL,
	[Annee] [nvarchar](255) NULL,
	[num_carte_soin] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSCotisantCNSS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSCotisantCNSS](
	[ID] [nvarchar](255) NULL,
	[ASS_MAT] [nvarchar](255) NULL,
	[ASS_CLE] [nvarchar](255) NULL,
	[BEN_DTNAIS] [nvarchar](255) NULL,
	[ASS_DTEFF] [nvarchar](255) NULL,
	[BEN_NUMID] [nvarchar](255) NULL,
	[BEN_SITFAM] [nvarchar](255) NULL,
	[NBENF] [nvarchar](255) NULL,
	[SU] [nvarchar](255) NULL,
	[TAUX_ATMP_INDEP] [nvarchar](255) NULL,
	[SIT_COT] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[LOC_CODPOS] [nvarchar](255) NULL,
	[ATM_REF] [nvarchar](255) NULL,
	[PAT_NUM] [nvarchar](255) NULL,
	[PRF_COD] [nvarchar](255) NULL,
	[PRF_ID] [nvarchar](255) NULL,
	[NBTRIM_DEC] [nvarchar](255) NULL,
	[NBTRIM_VAL] [nvarchar](255) NULL,
	[SIT_DAT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSCouvertureCnam]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSCouvertureCnam](
	[BEN_DATN] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[BEN_FAM] [nvarchar](255) NULL,
	[SIT_COD] [nvarchar](255) NULL,
	[MND_CIN] [nvarchar](255) NULL,
	[BEN_SEXE] [nvarchar](255) NULL,
	[LOC_COD] [nvarchar](255) NULL,
	[BEN_BUR] [nvarchar](255) NULL,
	[PID_TYP] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[TYPE] [nvarchar](255) NULL,
	[REGIME_CNSS] [nvarchar](255) NULL,
	[EMP_MAT] [nvarchar](255) NULL,
	[ROW_NUM] [nvarchar](255) NULL,
	[SECTEUR_ACTIVITE] [nvarchar](255) NULL,
	[FIL_COD] [nvarchar](255) NULL,
	[FIL_DDEB] [nvarchar](255) NULL,
	[GOUV_COD] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSDbssAssure]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSDbssAssure](
	[IU_BNF] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_RAC] [nvarchar](255) NULL,
	[ASS_SIT] [nvarchar](255) NULL,
	[ASS_CPT] [nvarchar](255) NULL,
	[DATE_CRE_IU] [nvarchar](255) NULL,
	[DATE_CRE] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSDbssBeneficiaire]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSDbssBeneficiaire](
	[IU_BNF] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_RAC] [nvarchar](255) NULL,
	[ASS_SIT] [nvarchar](255) NULL,
	[ASS_CPT] [nvarchar](255) NULL,
	[DATE_CRE_IU] [nvarchar](255) NULL,
	[DATE_CRE] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[ExecID] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSEmployeur]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSEmployeur](
	[MAT] [nvarchar](255) NULL,
	[CLE] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[ATV_COD] [nvarchar](255) NULL,
	[ADM_COD] [nvarchar](255) NULL,
	[SIT_EMP] [nvarchar](255) NULL,
	[DTEFF] [nvarchar](255) NULL,
	[DT_RADIATION] [nvarchar](255) NULL,
	[PAT_NUM] [nvarchar](255) NULL,
	[ACT_NAT] [nvarchar](255) NULL,
	[RRC] [nvarchar](255) NULL,
	[DATE_RRC] [nvarchar](255) NULL,
	[EXO_DTDEB] [nvarchar](255) NULL,
	[EXO_DTFIN] [nvarchar](255) NULL,
	[EXO_COD_EMP] [nvarchar](255) NULL,
	[LOC_LOC_CODPOS] [nvarchar](255) NULL,
	[RAIS] [nvarchar](255) NULL,
	[ATM_REF] [nvarchar](255) NULL,
	[TAUX_ATMP_EMP] [nvarchar](255) NULL,
	[COTISATION_ATMP] [nvarchar](255) NULL,
	[BAT_TAU] [nvarchar](255) NULL,
	[BAT_TYP] [nvarchar](255) NULL,
	[BAT_DTDEB] [nvarchar](255) NULL,
	[BAT_DTFIN] [nvarchar](255) NULL,
	[REG_COD] [nvarchar](255) NULL,
	[REG_LIB] [nvarchar](255) NULL,
	[DTNSIT] [nvarchar](255) NULL,
	[PAT_CLE] [nvarchar](255) NULL,
	[EMP_DERADR] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSHistoriqueIU]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSHistoriqueIU](
	[IU_NEW] [nvarchar](255) NULL,
	[IU_OLD] [nvarchar](255) NULL,
	[LOT_CRE] [nvarchar](255) NULL,
	[USE_CRE] [nvarchar](255) NULL,
	[DAT_CRE] [nvarchar](255) NULL,
	[TYPE_OPERATION] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSIndemniteDeces]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSIndemniteDeces](
	[MATRICULE] [nvarchar](255) NULL,
	[DATE_NAISSANCE] [nvarchar](255) NULL,
	[DATE_CREATION] [nvarchar](255) NULL,
	[DATE_DéCèS] [nvarchar](255) NULL,
	[TAUXCD] [nvarchar](255) NULL,
	[POSITION_AU_DéCèS] [nvarchar](255) NULL,
	[NOMBRE_ENFANTS] [nvarchar](255) NULL,
	[ASSIETTE] [nvarchar](255) NULL,
	[CAPITAL_BRUT] [nvarchar](255) NULL,
	[CAPITAL_NET] [nvarchar](255) NULL,
	[ETABLISSEMENT] [nvarchar](255) NULL,
	[LIBELLE_ETAB] [nvarchar](255) NULL,
	[GRADE] [nvarchar](255) NULL,
	[LIBELLE_GRADE] [nvarchar](255) NULL,
	[CADRE_ACTIF] [nvarchar](255) NULL,
	[MILITAIRE_BONIF] [nvarchar](255) NULL,
	[FONCTION_ASTREIGNANTE] [nvarchar](255) NULL,
	[FONCTION_PENIBLE] [nvarchar](255) NULL,
	[SOUS_POSITION] [nvarchar](255) NULL,
	[PERIODE_SOUS_POSITION] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSMembreMenage]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSMembreMenage](
	[lib_gouv] [nvarchar](255) NULL,
	[lib_del] [nvarchar](255) NULL,
	[id_gouv] [nvarchar](255) NULL,
	[id_del] [nvarchar](255) NULL,
	[code_postal_s] [nvarchar](255) NULL,
	[num_compte] [nvarchar](255) NULL,
	[status] [nvarchar](255) NULL,
	[ident_uni_chef] [nvarchar](255) NULL,
	[id_membre] [nvarchar](255) NULL,
	[id_type_rela] [nvarchar](255) NULL,
	[ident_uni] [nvarchar](255) NULL,
	[n_cin] [nvarchar](255) NULL,
	[id_typeidentifiant] [nvarchar](255) NULL,
	[nom_mem] [nvarchar](255) NULL,
	[prenom_mem] [nvarchar](255) NULL,
	[prenom_pere] [nvarchar](255) NULL,
	[prenom_grand_pere] [nvarchar](255) NULL,
	[nom_mere] [nvarchar](255) NULL,
	[prenom_mere] [nvarchar](255) NULL,
	[sexe] [nvarchar](255) NULL,
	[date_nais_mem] [nvarchar](255) NULL,
	[id_etat_civil] [nvarchar](255) NULL,
	[date_creation] [nvarchar](255) NULL,
	[date_modif] [nvarchar](255) NULL,
	[a_handicap] [nvarchar](255) NULL,
	[lib] [nvarchar](255) NULL,
	[situation] [nvarchar](255) NULL,
	[annee] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSPensionCNRPS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSPensionCNRPS](
	[ANNEE] [nvarchar](255) NULL,
	[MOIS] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[LIT] [nvarchar](255) NULL,
	[regime] [nvarchar](255) NULL,
	[etab] [nvarchar](255) NULL,
	[DATE_NAISSANCE] [nvarchar](255) NULL,
	[sitfam] [nvarchar](255) NULL,
	[djoui] [nvarchar](255) NULL,
	[dmar] [nvarchar](255) NULL,
	[motifmar] [nvarchar](255) NULL,
	[service] [nvarchar](255) NULL,
	[taux] [nvarchar](255) NULL,
	[nb_enfants] [nvarchar](255) NULL,
	[bonif] [nvarchar](255) NULL,
	[coord] [nvarchar](255) NULL,
	[brut] [nvarchar](255) NULL,
	[net] [nvarchar](255) NULL,
	[rappel] [nvarchar](255) NULL,
	[code_centre] [nvarchar](255) NULL,
	[postal] [nvarchar](255) NULL,
	[code_gouv] [nvarchar](255) NULL,
	[libelle_gouv] [nvarchar](255) NULL,
	[code_delegation] [nvarchar](255) NULL,
	[delegation] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSPensionCNSS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSPensionCNSS](
	[REGIME] [nvarchar](255) NULL,
	[CPT] [nvarchar](255) NULL,
	[NUM_ASS] [nvarchar](255) NULL,
	[RIS] [nvarchar](255) NULL,
	[RANG] [nvarchar](255) NULL,
	[ID] [nvarchar](255) NULL,
	[MOIS_PAYEMENT] [nvarchar](255) NULL,
	[MT_PENS_BRUT] [nvarchar](255) NULL,
	[MT_IMPOT] [nvarchar](255) NULL,
	[MT_NET] [nvarchar](255) NULL,
	[SF] [nvarchar](255) NULL,
	[CODE_POSTAL] [nvarchar](255) NULL,
	[CODE_RETRAITE] [nvarchar](255) NULL,
	[ENTREE_JUISSANCE] [nvarchar](255) NULL,
	[DATE_DECES] [nvarchar](255) NULL,
	[NBR_ENFANT] [nvarchar](255) NULL,
	[NBR_MOIS_VALIDE] [nvarchar](255) NULL,
	[CD_DEROG] [nvarchar](255) NULL,
	[TAUX_CALCULE] [nvarchar](255) NULL,
	[NBR_POINT_COMPLEMENTAIRE] [nvarchar](255) NULL,
	[SALAIRE_MOYEN_REFERENCE] [nvarchar](255) NULL,
	[CODE_BUREAU] [nvarchar](255) NULL,
	[TYPE_PENSION] [nvarchar](255) NULL,
	[PENSION_SERVIE] [nvarchar](255) NULL,
	[PENSION_BASE_DA ] [nvarchar](255) NULL,
	[DTNAIS] [nvarchar](255) NULL,
	[GENRE] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSPubliqueActe]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSPubliqueActe](
	[SEX] [nvarchar](255) NULL,
	[PRF_COD] [nvarchar](255) NULL,
	[PRF_CLE] [nvarchar](255) NULL,
	[PRF_TYP] [nvarchar](255) NULL,
	[VIREMENT] [nvarchar](255) NULL,
	[HOPITAL] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_REF] [nvarchar](255) NULL,
	[FAC_BRP] [nvarchar](255) NULL,
	[FAC_DATE] [nvarchar](255) NULL,
	[FAC_MNT] [nvarchar](255) NULL,
	[FAC_DATS] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[FAC_ACTE] [nvarchar](255) NULL,
	[FAC_ASSIU] [nvarchar](255) NULL,
	[LIEN] [nvarchar](255) NULL,
	[FAC_BENRANG] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[FAC_BORDANN] [nvarchar](255) NULL,
	[FAC_BORDMOIS] [nvarchar](255) NULL,
	[REG_NAT] [nvarchar](255) NULL,
	[REG_COD] [nvarchar](255) NULL,
	[FAC_TIKET] [nvarchar](255) NULL,
	[FAC_DATSOINS] [nvarchar](255) NULL,
	[BEN_DATN] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSPubliqueConsultation]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSPubliqueConsultation](
	[VIREMENT] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[LIEN] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[DCP_ANN] [nvarchar](255) NULL,
	[HOP_COD] [nvarchar](255) NULL,
	[LIBELE] [nvarchar](255) NULL,
	[DCP_ORD] [nvarchar](255) NULL,
	[SPE_COD] [nvarchar](255) NULL,
	[SPECIALITE] [nvarchar](255) NULL,
	[CONS_NUM] [nvarchar](255) NULL,
	[DATCONSULT] [nvarchar](255) NULL,
	[CONS_MAT] [nvarchar](255) NULL,
	[CONS_DATN] [nvarchar](255) NULL,
	[CONS_MNT] [nvarchar](255) NULL,
	[TICKET] [nvarchar](255) NULL,
	[BUR] [nvarchar](255) NULL,
	[LIEU] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[ExecID] [int] NULL,
	[SEX] [nvarchar](255) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSPubliqueHospitalisation]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSPubliqueHospitalisation](
	[VIREMENT] [nvarchar](255) NULL,
	[FAC_ANN] [nvarchar](255) NULL,
	[FAC_MNT] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[LIEN] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[HOP_COD] [nvarchar](255) NULL,
	[LIBELE] [nvarchar](255) NULL,
	[FAC_ORD] [nvarchar](255) NULL,
	[FAC_DATN] [nvarchar](255) NULL,
	[DATENTREE] [nvarchar](255) NULL,
	[DATSORTIE] [nvarchar](255) NULL,
	[TCKET] [nvarchar](255) NULL,
	[ACT_CNAM1] [nvarchar](255) NULL,
	[FAC_MAT] [nvarchar](255) NULL,
	[FAC_CLE] [nvarchar](255) NULL,
	[BUR] [nvarchar](255) NULL,
	[LIEU] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRegimeComplementaire]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRegimeComplementaire](
	[ANNEE] [nvarchar](255) NULL,
	[EMP_MAT] [nvarchar](255) NULL,
	[EMP_CLE] [nvarchar](255) NULL,
	[NUMASS] [nvarchar](255) NULL,
	[IU] [nvarchar](255) NULL,
	[NBPOINT] [nvarchar](255) NULL,
	[NPSTRI] [nvarchar](255) NULL,
	[NPSTRA] [nvarchar](255) NULL,
	[CODREDR] [nvarchar](255) NULL,
	[CODSIT] [nvarchar](255) NULL,
	[LOC_CODPOS] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[EMP_DTREGCP] [nvarchar](255) NULL,
	[EMP_DTFINREGCP] [nvarchar](255) NULL,
	[ANN_EFFET_ASS] [nvarchar](255) NULL,
	[SALDEC] [nvarchar](255) NULL,
	[NBJC] [nvarchar](255) NULL,
	[NBJRI] [nvarchar](255) NULL,
	[NBJRA] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRemboursementActe]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRemboursementActe](
	[CAISSE] [nvarchar](255) NULL,
	[ANNEE_EXERCICE] [nvarchar](255) NULL,
	[STR_COD] [nvarchar](255) NULL,
	[DOS_DAT] [nvarchar](255) NULL,
	[DOS_NUM] [nvarchar](255) NULL,
	[REF_BS] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[IDENTIFIAT_UNIQUE] [nvarchar](255) NULL,
	[TYPE_BENEFICIAIRE] [nvarchar](255) NULL,
	[AGE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[REGIMEBS] [nvarchar](255) NULL,
	[MNT_REEL] [nvarchar](255) NULL,
	[CODE_PRESTATAIRE] [nvarchar](255) NULL,
	[ACT_LET_CM] [nvarchar](255) NULL,
	[ACTE] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[LIBELLE_ACTE] [nvarchar](1000) NULL,
	[DATE_ACTE] [nvarchar](255) NULL,
	[ACT_REMB] [nvarchar](255) NULL,
	[ACT_PAYE] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRemboursementAppareillage]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRemboursementAppareillage](
	[CAISSE] [nvarchar](255) NULL,
	[ANNEE_EXERCICE] [nvarchar](255) NULL,
	[STR_COD] [nvarchar](255) NULL,
	[DOS_DAT] [nvarchar](255) NULL,
	[DOS_NUM] [nvarchar](255) NULL,
	[REF_BS] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[IDENTIFIAT_UNIQUE] [nvarchar](255) NULL,
	[TYPE_BENEFICIAIRE] [nvarchar](255) NULL,
	[AGE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[REGIMEBS] [nvarchar](255) NULL,
	[MNT_REEL] [nvarchar](255) NULL,
	[CODE_APPAREIL] [nvarchar](255) NULL,
	[APPAREIL] [nvarchar](255) NULL,
	[DATE_ACHAT_APP] [nvarchar](255) NULL,
	[MNT_REMB] [nvarchar](255) NULL,
	[MNT_PAY] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRemboursementBulletinSoin]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRemboursementBulletinSoin](
	[BUR_INT] [nvarchar](255) NULL,
	[STR_COD] [nvarchar](255) NULL,
	[DOS_DAT] [nvarchar](255) NULL,
	[DOS_NUM] [nvarchar](255) NULL,
	[REF_BS] [nvarchar](255) NULL,
	[CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[IDENTIFIANT_UNIQUE] [nvarchar](255) NULL,
	[TYPE_BENEFICIAIRE] [nvarchar](255) NULL,
	[AGE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[REGIMEBS] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[REG_LIB] [nvarchar](255) NULL,
	[FILIERE] [nvarchar](255) NULL,
	[DATE_DEPOT] [nvarchar](255) NULL,
	[DAT_DEB_SOINS] [nvarchar](255) NULL,
	[APCI_COD] [nvarchar](255) NULL,
	[TOTAL_PAYE_BS] [nvarchar](255) NULL,
	[TOTAL_REMB_BS] [nvarchar](255) NULL,
	[TOTAL_PAYE_ACT] [nvarchar](255) NULL,
	[TOTAL_REMB_ACT] [nvarchar](255) NULL,
	[TOTAL_PAYE_MED] [nvarchar](255) NULL,
	[TOTAL_REMB_MED] [nvarchar](255) NULL,
	[TOTAL_PAYE_VISITE] [nvarchar](255) NULL,
	[TOTAL_REMB_VISITE] [nvarchar](255) NULL,
	[TOTAL_PAYE_APP] [nvarchar](255) NULL,
	[TOTAL_REMB_APP] [nvarchar](255) NULL,
	[DATE_OP_TECHNIQUE] [nvarchar](255) NULL,
	[DATE_OP_COMPTABLE] [nvarchar](255) NULL,
	[DATE_VIREMENT] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRemboursementConsultation]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRemboursementConsultation](
	[CAISSE] [nvarchar](255) NULL,
	[ANNEE_EXERCICE] [nvarchar](255) NULL,
	[STR_COD] [nvarchar](255) NULL,
	[DOS_DAT] [nvarchar](255) NULL,
	[DOS_NUM] [nvarchar](255) NULL,
	[REF_BS] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[IDENTIFIAT_UNIQUE] [nvarchar](255) NULL,
	[TYPE_BENEFICIAIRE] [nvarchar](255) NULL,
	[AGE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[REGIMEBS] [nvarchar](255) NULL,
	[NAT_COD] [nvarchar](255) NULL,
	[NAT_LIB] [nvarchar](255) NULL,
	[DATE_CONSULTATION] [nvarchar](255) NULL,
	[CODE_PRESCRIPTEUR] [nvarchar](255) NULL,
	[MNT_PAY] [nvarchar](255) NULL,
	[MONTANT_REEL] [nvarchar](255) NULL,
	[MONTANT_REMBOURSE] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSRemboursementMedicament]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSRemboursementMedicament](
	[CAISSE] [nvarchar](255) NULL,
	[ANNEE_EXERCICE] [nvarchar](255) NULL,
	[STR_COD] [nvarchar](255) NULL,
	[DOS_DAT] [nvarchar](255) NULL,
	[DOS_NUM] [nvarchar](255) NULL,
	[REF_BS] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[IDENTIFIAT_UNIQUE] [nvarchar](255) NULL,
	[TYPE_BENEFICIAIRE] [nvarchar](255) NULL,
	[AGE] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[REGIMEBS] [nvarchar](255) NULL,
	[MED_TOTREMB] [nvarchar](255) NULL,
	[MDC_TYP_CM] [nvarchar](255) NULL,
	[CODE_PCT] [nvarchar](255) NULL,
	[LIB_MEDICAMENT] [nvarchar](255) NULL,
	[GENERIQUE] [nvarchar](255) NULL,
	[MNT_REEL] [nvarchar](255) NULL,
	[MONTANT_PAYE] [nvarchar](255) NULL,
	[QUANTITE] [nvarchar](255) NULL,
	[CODE_PRESTATAIRE] [nvarchar](255) NULL,
	[DATE_ACHAT] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSSalaireCNRPS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSSalaireCNRPS](
	[matricul] [nvarchar](255) NULL,
	[CIN] [nvarchar](255) NULL,
	[sexe] [nvarchar](255) NULL,
	[date_naissance] [nvarchar](255) NULL,
	[sitfam] [nvarchar](255) NULL,
	[postal] [nvarchar](255) NULL,
	[date_affiliation] [nvarchar](255) NULL,
	[date_recrut] [nvarchar](255) NULL,
	[pos_admin] [nvarchar](255) NULL,
	[code_etab_payeur] [nvarchar](255) NULL,
	[libelle_etab] [nvarchar](255) NULL,
	[Colonne 12] [nvarchar](255) NULL,
	[code_grade] [nvarchar](255) NULL,
	[code_fonction] [nvarchar](255) NULL,
	[annee] [nvarchar](255) NULL,
	[periode] [nvarchar](255) NULL,
	[perd] [nvarchar](255) NULL,
	[code_indem1] [nvarchar](255) NULL,
	[montant_indem1] [nvarchar](255) NULL,
	[code_indem2] [nvarchar](255) NULL,
	[montant_indem2] [nvarchar](255) NULL,
	[code_indem3] [nvarchar](255) NULL,
	[montant_indem3] [nvarchar](255) NULL,
	[code_indem4] [nvarchar](255) NULL,
	[montant_indem4] [nvarchar](255) NULL,
	[code_indem5] [nvarchar](255) NULL,
	[montant_indem5] [nvarchar](255) NULL,
	[code_indem6] [nvarchar](255) NULL,
	[montant_indem6] [nvarchar](255) NULL,
	[code_indem7] [nvarchar](255) NULL,
	[montant_indem7] [nvarchar](255) NULL,
	[code_indem8] [nvarchar](255) NULL,
	[montant_indem8] [nvarchar](255) NULL,
	[code_indem9] [nvarchar](255) NULL,
	[montant_indem9] [nvarchar](255) NULL,
	[code_indem10] [nvarchar](255) NULL,
	[montant_indem10] [nvarchar](255) NULL,
	[code_indem11] [nvarchar](255) NULL,
	[montant_indem11] [nvarchar](255) NULL,
	[code_indem12] [nvarchar](255) NULL,
	[montant_indem12] [nvarchar](255) NULL,
	[code_indem13] [nvarchar](255) NULL,
	[montant_indem13] [nvarchar](255) NULL,
	[code_indem14] [nvarchar](255) NULL,
	[montant_indem14] [nvarchar](255) NULL,
	[code_indem15] [nvarchar](255) NULL,
	[montant_indem15] [nvarchar](255) NULL,
	[code_indem16] [nvarchar](255) NULL,
	[montant_indem16] [nvarchar](255) NULL,
	[code_indem17] [nvarchar](255) NULL,
	[montant_indem17] [nvarchar](255) NULL,
	[code_indem18] [nvarchar](255) NULL,
	[montant_indem18] [nvarchar](255) NULL,
	[code_indem19] [nvarchar](255) NULL,
	[montant_indem19] [nvarchar](255) NULL,
	[code_indem20] [nvarchar](255) NULL,
	[montant_indem20] [nvarchar](255) NULL,
	[Colonne 58] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSSalaireCNSS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSSalaireCNSS](
	[ID] [nvarchar](255) NULL,
	[ASS_MAT] [nvarchar](255) NULL,
	[ASS_CLE] [nvarchar](255) NULL,
	[REG_COD] [nvarchar](255) NULL,
	[EMP_MAT] [nvarchar](255) NULL,
	[EMP_CLE] [nvarchar](255) NULL,
	[ANNEE] [nvarchar](255) NULL,
	[TRIMESTRE] [nvarchar](255) NULL,
	[CODE_TYPE_SALAIRE] [nvarchar](255) NULL,
	[SALAIRE] [nvarchar](255) NULL,
	[DATE_SAISIE] [nvarchar](255) NULL,
	[CAR_CAT_INDEP] [nvarchar](255) NULL,
	[SIT_EMP] [nvarchar](255) NULL,
	[EXO_DTDEB] [nvarchar](255) NULL,
	[EXO_DTFIN] [nvarchar](255) NULL,
	[EXO_COD_EMP] [nvarchar](255) NULL,
	[TAUX_ATMP_EMP] [nvarchar](255) NULL,
	[sit_cot] [nvarchar](255) NULL,
	[taux_atmp_indep] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSStqbrCNSS]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSStqbrCNSS](
	[Annee] [nvarchar](255) NULL,
	[MATRICULE] [nvarchar](255) NULL,
	[SIT_FAM] [nvarchar](255) NULL,
	[t1] [nvarchar](255) NULL,
	[t2] [nvarchar](255) NULL,
	[t3] [nvarchar](255) NULL,
	[t4] [nvarchar](255) NULL,
	[NBRE_2_3_SMIG] [nvarchar](255) NULL,
	[NBRE_1_SMIG] [nvarchar](255) NULL,
	[DER_AN_DEC] [nvarchar](255) NULL,
	[DER_TRIM_DEC] [nvarchar](255) NULL,
	[TOT_DEC] [nvarchar](255) NULL,
	[situation] [nvarchar](255) NULL,
	[CATEGORIE] [nvarchar](255) NULL,
	[REGIME] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSTiersPayantActe]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSTiersPayantActe](
	[FILIERE] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[BOR_ANN] [nvarchar](255) NULL,
	[FAC_ORD] [nvarchar](255) NULL,
	[BOR_ORD] [nvarchar](255) NULL,
	[PRF_COD] [nvarchar](255) NULL,
	[PRF_CLE] [nvarchar](255) NULL,
	[PRF_TYP] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[DATNAIS] [nvarchar](255) NULL,
	[FAC_DEXEC] [nvarchar](255) NULL,
	[VIREMENT] [nvarchar](255) NULL,
	[PRESCRIPTEUR] [nvarchar](255) NULL,
	[PRF_CODB] [nvarchar](255) NULL,
	[PRF_CLEB] [nvarchar](255) NULL,
	[PRF_TYPB] [nvarchar](255) NULL,
	[EXECUTEUR] [nvarchar](255) NULL,
	[DATPRESCRIP] [nvarchar](255) NULL,
	[ACT_COD] [nvarchar](255) NULL,
	[NOMBRE] [nvarchar](255) NULL,
	[DEMANDE] [nvarchar](255) NULL,
	[REMBOURSE] [nvarchar](255) NULL,
	[PERCU] [nvarchar](255) NULL,
	[FAC_ETA] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSTiersPayantConsultation]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSTiersPayantConsultation](
	[FILIERE] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[BOR_ANN] [nvarchar](255) NULL,
	[FAC_ORD] [nvarchar](255) NULL,
	[BOR_ORD] [nvarchar](255) NULL,
	[PRF_COD] [nvarchar](255) NULL,
	[PRF_CLE] [nvarchar](255) NULL,
	[PRF_TYP] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[DATNAIS] [nvarchar](255) NULL,
	[FAC_DPRES] [nvarchar](255) NULL,
	[FAC_DEXEC] [nvarchar](255) NULL,
	[BEN_DATN] [nvarchar](255) NULL,
	[CNS_DAT] [nvarchar](255) NULL,
	[CNS_TYP] [nvarchar](255) NULL,
	[CNS_MNT] [nvarchar](255) NULL,
	[CNS_PRC] [nvarchar](255) NULL,
	[FAC_CONS_PAY] [nvarchar](255) NULL,
	[BOR_DATS] [nvarchar](255) NULL,
	[VIREMENT] [nvarchar](255) NULL,
	[FAC_CONS_ETA] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSTiersPayantMedicament]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSTiersPayantMedicament](
	[FILIERE] [nvarchar](255) NULL,
	[SEX] [nvarchar](255) NULL,
	[IU_BNF] [nvarchar](255) NULL,
	[BUR_COD] [nvarchar](255) NULL,
	[BOR_ANN] [nvarchar](255) NULL,
	[FAC_ORD] [nvarchar](255) NULL,
	[BOR_ORD] [nvarchar](255) NULL,
	[PRF_COD] [nvarchar](255) NULL,
	[PRF_CLE] [nvarchar](255) NULL,
	[PRF_TYP] [nvarchar](255) NULL,
	[CODE_CAISSE] [nvarchar](255) NULL,
	[ASS_IU] [nvarchar](255) NULL,
	[BEN_TYPE] [nvarchar](255) NULL,
	[BEN_RANG] [nvarchar](255) NULL,
	[DATNAIS] [nvarchar](255) NULL,
	[FAC_DEXEC] [nvarchar](255) NULL,
	[VIREMENT] [nvarchar](255) NULL,
	[PRESCRIPTEUR] [nvarchar](255) NULL,
	[PRF_CODB] [nvarchar](255) NULL,
	[PRF_CLEB] [nvarchar](255) NULL,
	[PRF_TYPB] [nvarchar](255) NULL,
	[EXECUTEUR] [nvarchar](255) NULL,
	[DATPRESCRIP] [nvarchar](255) NULL,
	[MDC_COD] [nvarchar](255) NULL,
	[DUREE] [nvarchar](255) NULL,
	[QUANTITE] [nvarchar](255) NULL,
	[DEMANDE] [nvarchar](255) NULL,
	[PAYE] [nvarchar](255) NULL,
	[REMBOURSE] [nvarchar](255) NULL,
	[PERCU] [nvarchar](255) NULL,
	[FAC_ETA] [nvarchar](255) NULL,
	[ExecID] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ODSTransfertMonetairePermanent]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ODSTransfertMonetairePermanent](
	[CNSS] [nvarchar](255) NULL,
	[CIN] [nvarchar](255) NULL,
	[J_NAIS] [nvarchar](255) NULL,
	[M_NAIS] [nvarchar](255) NULL,
	[A_NAIS] [nvarchar](255) NULL,
	[JBEN] [nvarchar](255) NULL,
	[MBENEF] [nvarchar](255) NULL,
	[ABENEF] [nvarchar](255) NULL,
	[SEXE] [nvarchar](255) NULL,
	[SIT_FAM] [nvarchar](255) NULL,
	[GOUV] [nvarchar](255) NULL,
	[DELEG] [nvarchar](255) NULL,
	[IDENTITE] [nvarchar](255) NULL,
	[ADRESSE] [nvarchar](255) NULL,
	[CODE_POS] [nvarchar](255) NULL,
	[LOCALITE] [nvarchar](255) NULL,
	[MAND] [nvarchar](255) NULL,
	[NBRE_ENF_S] [nvarchar](255) NULL,
	[NBRE_ENF_H] [nvarchar](255) NULL,
	[ID_SOCIAL] [nvarchar](255) NULL,
	[ExecID] [int] NULL,
	[Annee] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[RejetOdsChefMenage]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[RejetOdsChefMenage](
	[Colonne de sortie d'erreur de source de fichier plat] [varchar](max) NULL,
	[ErrorCode] [int] NULL,
	[ErrorColumn] [int] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[test_consultation_publique]    Script Date: 03/03/2026 11:03:04 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[test_consultation_publique](
	[VIREMENT] [varchar](4000) NULL,
	[CAISSE] [varchar](8) NULL,
	[LIEN] [varchar](9) NULL,
	[REGIME] [varchar](4000) NULL,
	[DCP_ANN] [nvarchar](255) NULL,
	[HOP_COD] [nvarchar](255) NULL,
	[LIBELE] [varchar](4000) NULL,
	[DCP_ORD] [nvarchar](255) NULL,
	[SPE_COD] [nvarchar](255) NULL,
	[SPECIALITE] [varchar](4000) NULL,
	[CONS_NUM] [nvarchar](255) NULL,
	[DATCONSULT] [nvarchar](255) NULL,
	[CONS_MAT] [nvarchar](255) NULL,
	[CONS_DATN] [nvarchar](255) NULL,
	[CONS_MNT] [nvarchar](255) NULL,
	[TICKET] [nvarchar](255) NULL,
	[BUR] [nvarchar](255) NULL,
	[LIEU] [varchar](4000) NULL
) ON [PRIMARY]
GO
