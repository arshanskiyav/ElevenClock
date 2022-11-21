﻿; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ElevenClock"
#define MyAppVersion "3.9.5"
#define MyAppPublisher "Martí Climent"
#define MyAppURL "https://github.com/martinet101/ElevenClock"
#define MyAppExeName "ElevenClock.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.) 
AppId={{D62480B8-71F1-48CE-BEEC-9D3E172C87B5}
AppName={#MyAppName}
DisableWelcomePage=no
AppVersion={#MyAppVersion}
AppVerName={#MyAppName}
AppPublisher="Martí Climent"
AppPublisherURL="https://www.somepythonthings.tk/"
AppSupportURL="https://www.somepythonthings.tk/#contact"
AppUpdatesURL="https://github.com/martinet101/ElevenClock/releases"
DefaultDirName={autopf}\ElevenClock
DisableDirPage=yes
ChangesAssociations=yes
CloseApplications=no
ArchitecturesInstallIn64BitMode=x64 arm64
DisableProgramGroupPage=yes
MinVersion=10.0
LicenseFile=LICENSE
; Uncomment the following line to run in non administrative install mode (install for current user only.)
PrivilegesRequired=lowest
OutputDir=.\
OutputBaseFilename=ElevenClock.Installer
SetupIconFile=elevenclock\resources\icon.ico
UninstallDisplayIcon={app}\ElevenClock.exe
Compression=lzma
SolidCompression=yes
UsePreviousAppDir=no
WizardStyle=classic
WizardImageStretch=yes 
WizardImageFile=INSTALLER.BMP
WizardSmallImageFile=elevenclock\resources\icon.bmp

[Languages] 
Name: "English"; MessagesFile: "compiler:Default.isl"    
Name: "Armenian"; MessagesFile: "compiler:Languages\Armenian.isl"
Name: "BrazilianPortuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "Catalan"; MessagesFile: "compiler:Languages\Catalan.isl"
Name: "Corsican"; MessagesFile: "compiler:Languages\Corsican.isl"
Name: "Czech"; MessagesFile: "compiler:Languages\Czech.isl"
Name: "Danish"; MessagesFile: "compiler:Languages\Danish.isl"
Name: "Dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "Finnish"; MessagesFile: "compiler:Languages\Finnish.isl"
Name: "French"; MessagesFile: "compiler:Languages\French.isl"
Name: "German"; MessagesFile: "compiler:Languages\German.isl"
Name: "Hebrew"; MessagesFile: "compiler:Languages\Hebrew.isl"
Name: "Icelandic"; MessagesFile: "compiler:Languages\Icelandic.isl"
Name: "Italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "Japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "Norwegian"; MessagesFile: "compiler:Languages\Norwegian.isl"
Name: "Polish"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "Portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "Russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "Slovenian"; MessagesFile: "compiler:Languages\Slovenian.isl"
Name: "Spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "Turkish"; MessagesFile: "compiler:Languages\Turkish.isl"
Name: "Ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"

[UninstallRun]
Filename: "{cmd}"; Parameters: "/C ""taskkill /im ElevenClock.exe /f /t"

[InstallDelete]
Type: filesandordirs; Name: "{autopf}\ElevenClock\*"; BeforeInstall: TaskKill('ElevenClock.exe');

[UninstallDelete]  
Type: filesandordirs; Name: "{autopf}\ElevenClock\*"
Type: filesandordirs; Name: "{autopf}\ElevenClock392\*"


[Code]
procedure InitializeWizard;
begin
  WizardForm.Bevel.Visible := False;
  WizardForm.Bevel1.Visible := True;
end;

function InitializeUninstall(): Boolean;
var
  ErrorCode: Integer;
begin
  if CheckForMutexes('MyProgMutex') and
     (MsgBox('Application is running, do you want to close it?',
             mbConfirmation, MB_OKCANCEL) = IDOK) then
  begin
    Exec('taskkill.exe', '/f /im ElevenClock.exe', '', SW_HIDE, 
         ewWaitUntilTerminated, ErrorCode);
  end;

  Result := True;
end;

procedure TaskKill(FileName: String);
var
  ResultCode: Integer;
begin
    Exec('taskkill.exe', '/f /im ' + '"' + FileName + '"', '', SW_HIDE,
     ewWaitUntilTerminated, ResultCode);
end;

procedure RunUninstaller(Path: String);
var
  ResultCode: Integer;
begin
    Exec(ExpandConstant('{app}')+'\'+Path, ' /verysilent /SUPPRESSMSGBOXES', '', SW_HIDE,
     ewWaitUntilTerminated, ResultCode);
end;



[Registry]
Root: HKCU; Subkey: "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "elevenClock"; ValueData: """{app}\ElevenClock.exe"""; Flags: uninsdeletevalue

[Files]
Source: "ElevenClockBin/base_library.zip"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs 64bit ; BeforeInstall: RunUninstaller('unins.exe');
Source: "ElevenClockBin/ElevenClock.exe"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs 64bit ; BeforeInstall: TaskKill('ElevenClock.exe');
Source: "ElevenClockBin/*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs 64bit;
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName} Settings"; Filename: "{app}\{#MyAppExeName}"; Parameters: "--settings"
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}";

[Run]
Filename: "{app}\ElevenClock.exe"; Flags: dontlogparameters nowait postinstall;
