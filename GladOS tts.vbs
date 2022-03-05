Set shell = WScript.CreateObject("WScript.Shell")

ttsText = InputBox("Enter text below", "GladOS TTS")
If Len(ttsText) = 0 Then
	WScript.Quit
END If

Function URLEncode( StringVal )
  Dim i, CharCode, Char, Space
  Dim StringLen

  StringLen = Len(StringVal)
  ReDim result(StringLen)

  'Space = "+"
  Space = "%20"

  For i = 1 To StringLen
    Char = Mid(StringVal, i, 1)
    CharCode = AscW(Char)
    If 97 <= CharCode And CharCode <= 122 _
    Or 64 <= CharCode And CharCode <= 90 _
    Or 48 <= CharCode And CharCode <= 57 _
    Or 45 = CharCode _
    Or 46 = CharCode _
    Or 95 = CharCode _
    Or 126 = CharCode Then
      result(i) = Char
    ElseIf 32 = CharCode Then
      result(i) = Space
    Else
      result(i) = "&#" & CharCode & ";"
    End If
  Next
  URLEncode = Join(result, "")
End Function

Dim encodedText
encodedText = URLEncode(ttsText)
shell.Run("curl https://glados.c-net.org/generate?text=" & encodedText)
shell.Run( Chr(34)&"C:\Program Files\Other Apps\VLC\vlc"&Chr(34) & " https://glados.c-net.org/generate?text=" & encodedText)