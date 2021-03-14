var PANEL_HOME = [
  {
    width: 2,
    height: 4,
    items: [
      {
         position: [0, 1],
         type: TYPES.ALARM,
         title: 'Alarme',
         id: 'alarm_control_panel.ha_alarm',
         icons: {
            arming: 'mdi-bell-outline',
            disarmed: 'mdi-bell-off',
            pending: 'mdi-bell',
            armed_custom_bypass: 'mdi-bell-check',
            armed_home: 'mdi-bell-plus',
            armed_night: 'mdi-bell-sleep',
            armed_away: 'mdi-bell',
            triggered: 'mdi-bell-ring'
         },
         states: {
            arming: 'Arming',
            disarmed: 'Desarmado',
            pending: 'Pending',
            armed_custom_bypass: 'Armed (bypass)',
            armed_home: 'Armado (em casa)',
            armed_night: 'Armado (dormindo)',
            armed_away: 'Armado (ausente)',
            triggered: 'Triggered'
         }
      },
      {
         position: [0, 2],
         type: TYPES.SENSOR,
         title: 'Iluminação externa',
         id: 'sensor.lumens_garden_illuminance_lux',
         unit: 'lux', // override default entity unit
         state: false, // hidding state
         filter: function (value) { // optional
            var num = parseFloat(value);
            return num && !isNaN(num) ? num.toFixed(1) : value;
         }
      },
      {
         position: [1, 1],
         type: TYPES.SENSOR_ICON,
         title: 'Aurélio',
         id: 'sensor.tracker_aurelio',
         states: {
            home: 'Em casa',
            not_home: 'Ausente'
         },
         icons: {
            home: 'mdi-home-account',
            not_home: 'mdi-home-outline'
         },
      },
      {
         position: [1, 2],
         type: TYPES.SENSOR_ICON,
         title: 'Camila',
         id: 'sensor.tracker_camila',
         states: {
            home: 'Em casa',
            not_home: 'Ausente'
         },
         icons: {
            home: 'mdi-home-account',
            not_home: 'mdi-home-outline'
         },
      }
    ]
  },
  {
    width: 2,
    height: 4,
    items: [
      {
         position: [1, 1],
         type: TYPES.SENSOR_ICON,
         title: 'Portas',
         id: 'group.doors',
         states: {
            on: 'Abertas',
            off: 'Fechadas'
         },
         icons: {
            off: 'mdi-door-closed-lock',
            on: 'mdi-door-open'
         },
      },
      {
         position: [2, 1],
         type: TYPES.SENSOR_ICON,
         title: 'Janelas',
         id: 'group.windows',
         states: {
            on: 'Abertas',
            off: 'Fechadas'
         },
         icons: {
            off: 'mdi-window-closed-variant',
            on: 'mdi-window-open-variant'
         },
      },
      {
         position: [1, 2],
         width: 1,
         title: 'Notificações sonoras',
         classes: [CLASS_BIG],
         type: TYPES.INPUT_BOOLEAN,
         id: 'input_boolean.speech_notifications',
         icons: {
            on: 'mdi-volume-high',
            off: 'mdi-volume-off'
         },
         states: {
            on: "Ativado",
            off: "Desativado"
         }
      },
      {
         position: [2, 2],
         width: 1,
         title: 'Notificações',
         classes: [CLASS_BIG],
         type: TYPES.INPUT_BOOLEAN,
         id: 'input_boolean.text_notifications',
         icons: {
            on: 'mdi-message',
            off: 'mdi-message-off'
         },
         states: {
            on: "Ativado",
            off: "Desativado"
         }
      }
    ]
  }
];

console.log('teste');
