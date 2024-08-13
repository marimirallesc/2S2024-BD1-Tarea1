USE EmpleadosDB;  -- Asegúrate de usar la base de datos correcta
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE IF NOT EXISTS [dbo].[DBErrors](
    [ErrorID] [int] IDENTITY(1,1) NOT NULL PRIMARY KEY,
    [ErrorNumber] [int] NULL,
    [ErrorState] [int] NULL,
    [ErrorSeverity] [int] NULL,
    [ErrorLine] [int] NULL,
    [ErrorProcedure] [varchar](max) NULL,
    [ErrorMessage] [varchar](max) NULL,
    [ErrorDateTime] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
