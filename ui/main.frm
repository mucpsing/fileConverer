VERSION 5.00
Begin VB.Form MainForm 
   Caption         =   "Form1"
   ClientHeight    =   4335
   ClientLeft      =   120
   ClientTop       =   285
   ClientWidth     =   8745
   LinkTopic       =   "Form1"
   ScaleHeight     =   4335
   ScaleWidth      =   8745
   Begin VB.Frame mainListTitle 
      Caption         =   "文件列表"
      Height          =   3255
      Left            =   120
      TabIndex        =   1
      Top             =   120
      Width           =   8415
      Begin VB.ListBox mianList 
         Height          =   2580
         Left            =   120
         TabIndex        =   2
         Top             =   240
         Width           =   8175
      End
   End
   Begin VB.CommandButton mainBtn_run 
      Caption         =   "运     行"
      Height          =   735
      Left            =   120
      TabIndex        =   0
      Top             =   3480
      Width           =   8415
   End
End
Attribute VB_Name = "MainForm"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Text2_Change()

End Sub

Private Sub List1_Click()

End Sub

Private Sub mainBtn_run_Click()

End Sub

Private Sub mianList_Click()

End Sub
