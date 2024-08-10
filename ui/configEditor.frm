VERSION 5.00
Begin VB.Form ConfEditorForm 
   Caption         =   "ConfEditorForm"
   ClientHeight    =   7125
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4110
   LinkTopic       =   "Form2"
   ScaleHeight     =   7125
   ScaleWidth      =   4110
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Frame1 
      Caption         =   "配置编辑器"
      Height          =   6855
      Left            =   120
      TabIndex        =   0
      Top             =   120
      Width           =   3855
      Begin VB.CommandButton confEditorBtn_cannel 
         Caption         =   "取  消"
         Height          =   615
         Left            =   1920
         TabIndex        =   2
         Top             =   6120
         Width           =   1815
      End
      Begin VB.CommandButton confEditorBtn_save 
         Caption         =   "保  存"
         Height          =   615
         Left            =   120
         TabIndex        =   1
         Top             =   6120
         Width           =   1695
      End
   End
End
Attribute VB_Name = "ConfEditorForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub config_save_cannel_Click()

End Sub

Private Sub config_save_Click()

End Sub
