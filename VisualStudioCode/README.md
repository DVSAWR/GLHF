# VS COODE

## Settings (JSON)

```json
{
    //workbench settings
    "workbench.colorTheme": "Kanagawa Black",
    "workbench.sideBar.location": "right",

    "window.zoomLevel": 1,

    // editor settings
    "editor.fontFamily": "Iosevka, Consolas, 'Courier New', monospace",
    "editor.fontSize": 17,
    "editor.lineHeight": 22,
    "editor.fontLigatures": false,
    "editor.rulers": [79],
    "editor.wordWrap": "on",
    "editor.minimap.enabled": true,
    "editor.minimap.side": "left",
    "editor.minimap.autohide": true,
    // "editor.minimap.showSlider": "always",
    "editor.minimap.scale": 1,
    "editor.overviewRulerBorder": false,
    "editor.scrollbar.vertical": "hidden",
    "editor.bracketPairColorization.independentColorPoolPerBracketType": true,
    // "editor.formatOnSave": true,
    // "editor.defaultFormatter": "",

    // "terminal.integrated.fontFamily": "",
    "terminal.integrated.fontSize": 17,
    // delete end spaces
    "files.trimTrailingWhitespace": true,

    "security.allowedUNCHosts": [
        "wsl.localhost"
    ],

    "editor.unicodeHighlight.allowedLocales": {
        "ru": true
    },

    // Background colors
    "workbench.colorCustomizations": {
        "editor.selectionBackground": "#17ae8190",
        "editor.background": "#000000",
        "terminal.background": "#000000",
        "statusBar.background": "#050505",
        "sideBar.background": "#050505",
        "menu.background": "#050505",
        "activityBar.background": "#050505",
        "titleBar.activeBackground": "#050505",
        "titleBar.inactiveBackground": "#050505",
        "panel.background": "#050505",
        "tab.activeBackground": "#050505",
        "tab.inactiveBackground": "#050505",
        "tab.activeBorder": "#050505",
        "tab.hoverBackground": "#050505",
        "quickInputList.focusBackground": "#050505",
        "editorGroupHeader.tabsBackground": "#050505",
        // BreacketsColors 1-6
        // "editorBracketHighlight.foreground1": "#ac86ff",
        // "editorBracketHighlight.foreground2": "#ffb134",
        // "editorBracketHighlight.foreground3": "#ffffff",
    },
    // color text settings
    "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": "comment",
        "settings": {
          "fontStyle": "italic"
        }
      },
      {
        "scope": "storage.type",
        "settings": {
          "fontStyle": "italic"
        }
      },
      {
        "scope": "variable.parameter",
        "settings": {
          // "foreground": "#ff0048",
          "fontStyle": "italic"
        }
      },
      {
        "scope": "support.type, support.class",
        "settings": {
          "fontStyle": ""
        }
      },
      {
        "scope": "comment",
        "settings": {
          "foreground": "#383838",
          "fontStyle": "italic"
        }
      },
      {
        "scope": "string.quoted.docstring.multi.python",
        "settings": {
          "foreground": "#383838",
          "fontStyle": "italic"
        }
      }
    ]
  },
  "terminal.integrated.fontFamily": "monospace",
  "workbench.iconTheme": "bearded-icons",
}
```
