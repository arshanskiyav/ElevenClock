# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3 = {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python Date and time values": "",
    "To disable the zero-padding effect, add a # in bethwwn the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "",
    "Apply": "",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "",
    "Set a custom date and time format": "",
    "(for advanced users only)": "",
    "Move this clock to the left": "",
    "Move this clock to the top": "",
    "Move this clock to the right": "",
    "Move this clock to the bottom": "",
    "Restore horizontal position": "",
    "Restore vertical position": "",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "",
    "Reset ElevenClock preferences to defaults": "",
    "Specify a minimum width for the clock": "",
    "Search on the settings": "",
    "No results were found": "",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "",
    "Enable low-cpu mode": "",
    "You might lose functionalities, like the notification counter or the dynamic background": "",
    "Clock position and size:": "",
    "Clock size preferences, position offset, clock at the left, etc.": "",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "",
    "View": "",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "",
    "Ok": "",
    "More Info": "",
    "About Qt": "",
    "Success": "",
    "The monitors were unblacklisted successfully.": "",
    "Now you should see the clock everywhere": "",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Uzdevumu pārvaldnieks",
    "Change date and time": "Mainīt datumu un laiku",
    "Notification settings": "Paziņojumu iestatījumi",
    "Updates, icon tray, language": "Atjauninājumi, ikonjosla, valoda",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Paslēpt paplašinātās opcijas no labā-klikšķa izvēlnes (nepieciešama pārstartēšana)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Pilnekrāna uzvedība, pulksteņa novietojums, primārā monitora pulkstenis, citi iestatījumi",
    'Add the "Show Desktop" button on the left corner of every clock': 'Pievienot pogu "Rādīt darbvirsmu" katra pulksteņa kreisajā stūrī',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Jums iespējams jauzstāda pielāgota fona krāsa, lai tas strādātu.&nbsp;Vairāk info <a href="{0}" style="color:DodgerBlue">ŠEIT</a>',
    "Clock's font, font size, font color and background, text alignment": "Pulksteņa fonts, fonta izmērs, fonta krāsa un fons, teksta novietojums",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Datuma formāts, laika formāts, sekundes, nedēļas diena, nedēļas numurs, reģionālie iestatījumi",
    "Testing features and error-fixing tools": "Testēšana un kļūdu labošanas rīki",
    "Language pack author(s), help translating ElevenClock": "Valodas pakas autors(i), palīdzēt iztulkot ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informācija, ziņot par kļūdu, nosūtīt ieteikumu, ziedot, par",
    "Log, debugging information": "Žurnāls, atkļūdošanas informācija",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Piespiest rādīt pulksteni ekrāna augšpusē",
    "Show the clock on the primary screen": "Rādīt pulksteni uz primārā ekrāna",
    "Use a custom font color": "Izmantot pielāgotu fonta krāsu",
    "Use a custom background color": "Izmantot pielāgotu fona krāsu",
    "Align the clock text to the center": "Centrēt pulksteņa tekstu",
    "Select custom color": "Izvēlēties pielāgotu krāsu",
    "Hide the clock when a program occupies all screens": "Paslēpt pulksteni, kad kāda programma aizņem visus ekrānus",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Izmantot pielāgotu fontu",
    "Use a custom font size": "Izmantot pielāgotu fonta izmēru",
    "Enable hide when multi-monitor fullscreen apps are running": "Paslēpt, kad darbojas vairāku monitoru pilnekrāna lietotnes",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> jābūt ieslēgtam, lai varētu mainīt šo iestatījumu",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> jābūt izslēgtam, lai varētu mainīt šo iestatījumu",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Šī opcija tika atspējota, jo tai vajadzētu darboties pēc noklusējuma. Ja tā nav, lūdzu ziņojiet par kļūdu)",
    "ElevenClock's language": "ElevenClock valoda"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Par Qt6 (PySide6)",
    "About": "Par",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternatīvs ne-SSL atjauninājumu serveris (tas varētu palīdzēt ar SSL kļūdām)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Labojumi un citas eksperimentālas opcijas: (Lietot TIKAI tad, ja kaut kas nedarbojas)",
    "Show week number on the clock": "Rādīt nedēļas numuru"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Paslēpt pulksteni, kad darbojas RDP klients vai Citrix Workspace",
    "Clock Appearance:": "Pulksteņa izskats:",
    "Force the clock to have black text": "Rādīt pulksteni ar melnu tekstu",
    " - It is required that the Dark Text checkbox is disabled": " - ir nepieciešams, lai tumšā teksta opcija būtu atspējota",
    "Debbugging information:": "Atkļūdošanas informācija",
    "Open ElevenClock's log": "Atvērt ElevenClock žurnālu",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Rādīt pulksteni uz primārā ekrāna (noderīgi, ja uzlikts lai pulksteni rāda kreisajā pusē)",
    "Show weekday on the clock"  :"Rādīt nedēļas dienu",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock iestatījumi", # Also settings title
    "Reload Clocks"             :"Pārlādēt pulksteņus",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Pārstartēt ElevenClock",
    "Hide ElevenClock"          :"Paslēpt ElevenClock",
    "Quit ElevenClock"          :"Iziet no ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Galvenie iestatījumi",
    "Automatically check for updates"                                                   :"Automātiski pārbaudīt atjauninājumus",
    "Automatically install available updates"                                           :"Automātiski instalēt pieejamos atjauninājumus",
    "Enable really silent updates"                                                      :"Iespējot ļoti klusus atjauninājumus",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Apiet atjauninājumu piegādātāja autentifikācijas pārbaudi (NAV IETEICAMS, UZ PAŠA ATBILDĪBU)",
    "Show ElevenClock on system tray"                                                   :"Rādīt ElevenClock sistēmas ikonjoslā",
    "Alternative clock alignment (may not work)"                                        :"Alternatīvi pulksteņa novietojumi (iespējams, var nedarboties)",
    "Change startup behaviour"                                                          :"Mainīt startēšanas uzvedību",
    "Change"                                                                            :"Mainīt",
    "<b>Update to the latest version!</b>"                                             :"<b>Atjaunināt uz jaunāko versiju!</b>",
    "Install update"                                                                    :"Instalēt atjauninājumu",
    
    #Clock settings
    "Clock Settings:"                                              :"Pulksteņa iestatījumi",
    "Hide the clock in fullscreen mode"                            :"Paslēpt pulksteni pilnekrāna režīmā",
    "Hide the clock when RDP client is active"                     :"Paslēpt pulksteni kad ir aktīvs RDP klients",
    "Force the clock to be at the bottom of the screen"            :"Piespiest rādīt pulksteni ekrāna apakšpusē",
    "Show the clock when the taskbar is set to hide automatically" :"Rādīt pulksteni kad ir iespējota uzdevumjoslas automātiskā paslēpšana",
    "Fix the hyphen/dash showing over the month"                   :"Izlabot domuzīmes rādīšanu pāri mēnesim",
    "Force the clock to have white text"                           :"Rādīt pulksteni ar baltu tekstu",
    "Show the clock at the left of the screen"                     :"Rādīt pulksteni ekrāna kreisajā pusē",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Datuma un laika iestatījumi",
    "Show seconds on the clock"                         :"Rādīt sekundes",
    "Show date on the clock"                            :"Rādīt datumu",
    "Show time on the clock"                            :"Rādīt laiku",
    "Change date and time format (Regional settings)"   :"Mainīt datuma un laika formātu (reģionālie iestatījumi)",
    "Regional settings"                                 :"Reģionālie iestatījumi",
    
    #About the language pack
    "About the language pack:"                  :"Par valodu paku",
    "Translated to English by martinet101"      :"Uz Latviešu valodu tulkoja shadow118", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Iztulko ElevenClock savā valodā",
    "Get started"                               :"Aiziet",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Par ElevenClock versiju {0}:",
    "View ElevenClock's homepage"               :"Skatīt ElevenClock mājaslapu",
    "Open"                                      :"Atvērt",
    "Report an issue/request a feature"         :"Ziņot par kļūdu",
    "Report"                                    :"Ziņot",
    "Support the dev: Give me a coffee☕"       :"Atbalsti izstrādātāju: uzsauc man kafiju☕",
    "Open page"                                 :"Atvērt lapu",
    "Icons by Icons8"                           :"Ikonas no Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Mājaslapa",
    "Close settings"                            :"Aizvērt iestatījumus",
    "Close"                                     :"Aizvērt",
}

lang = lang2_3
