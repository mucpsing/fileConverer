VERSION 5.00
Begin VB.Form MainForm 
   Caption         =   "Form1"
   ClientHeight    =   4965
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   8775
   LinkTopic       =   "Form1"
   ScaleHeight     =   4965
   ScaleWidth      =   8775
   Begin VB.CommandButton mainBtn_run 
      Caption         =   "运     行"
      Height          =   615
      Left            =   120
      TabIndex        =   4
      Top             =   4200
      Width           =   6375
   End
   Begin VB.CommandButton mainBtn_open_config_editor 
      Caption         =   "配置编辑器"
      Height          =   615
      Left            =   6600
      TabIndex        =   3
      Top             =   4200
      Width           =   1935
   End
   Begin VB.Frame Frame1 
      Caption         =   "配置文件路径"
      Height          =   975
      Left            =   120
      TabIndex        =   1
      Top             =   3120
      Width           =   8415
      Begin VB.TextBox Text1 
         Height          =   615
         Left            =   120
         TabIndex        =   2
         Top             =   240
         Width           =   8175
      End
   End
   Begin VB.CommandButton mainBtn_sel_file 
      Caption         =   "点击打开或者拖拽文件"
      Height          =   2895
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   8535
   End
End
Attribute VB_Name = "MainForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
