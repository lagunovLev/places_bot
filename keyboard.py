import json

main_keyboard = {
  "one_time": False,
  "inline": False,
  "buttons": [
    [
      {
          "action": {
            "type": "text",
            "label": "Поиск🔎"
          },
          "color": "primary"
      },
      {
          "action": {
            "type": "text",
            "label": "Популярные✨"
          },
          "color": "primary"
      },
    ],
    [
      {
          "action": {
            "type": "callback",
            "label": "Категории🗃️"
        }
      },
      {
        "action": {
          "type": "text",
          "label": "Случайное место🎲"
        }
      }
    ]
  ]
}
main_keyboard = json.dumps(main_keyboard)


empty = {
  "buttons": []
}
empty = json.dumps(empty)


searching = {
  "one_time": False,
  "inline": False,
  "buttons": [
    [
      {
          "action": {
            "type": "text",
            "label": "Отменить🚫"
          },
          "color": "primary"
      },
    ]
  ]
}
searching = json.dumps(searching)