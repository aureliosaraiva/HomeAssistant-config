var PANEL_POOL = [
  {
    width: 4,
    height: 4,
    items: [
      {
         position: [0, 1],
         type: TYPES.SENSOR_ICON,
         title: 'Filtro',
         id: 'binary_sensor.pool_pump_running',
         states: {
            on: 'Filtrando',
            off: 'Parada'
         },
         icons: {
            on: 'mdi-engine',
            off: 'mdi-engine-off'
         },
      },
      {
         position: [1, 1],
         type: TYPES.SENSOR,
         title: 'Uso hoje',
         id: 'sensor.pool_pump_running_today',
         state: false, // hidding state
      },
      {
         position: [2, 1],
         width: 1,
         title: 'Modo temporada',
         classes: [CLASS_BIG],
         type: TYPES.INPUT_BOOLEAN,
         id: 'input_boolean.swimming_season',
         icons: {
            on: 'mdi-swim',
            off: 'mdi-swim'
         },
         states: {
            on: "On",
            off: "Off"
         }
      },
      {
         position: [3, 1],
         type: TYPES.INPUT_SELECT,
         title: 'Modo',
         id: 'input_select.pool_pump',
         state: false
      }
    ]
  }
];
