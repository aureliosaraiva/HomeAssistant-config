var PANEL_BEDROOMS = [
  {
    width: 4,
    height: 4,
    items: [
      {
         position: [0, 1],
         type: TYPES.SENSOR,
         title: 'Suite',
         id: 'sensor.weather_bedroom_temperature',
         unit: '°C', // override default entity unit
         state: false, // hidding state
         filter: function (value) { // optional
            var num = parseFloat(value);
            return num && !isNaN(num) ? num.toFixed(1) : value;
         }
      },
      {
         position: [1, 1],
         type: TYPES.SENSOR,
         title: 'Banheiro (suite)',
         id: 'sensor.weather_bathroom_temperature',
         unit: '°C', // override default entity unit
         state: false, // hidding state
         filter: function (value) { // optional
            var num = parseFloat(value);
            return num && !isNaN(num) ? num.toFixed(1) : value;
         }
      },
      {
         position: [0, 2],
         title: 'Central',
         subtitle: 'Suite',
         id: 'switch.switch_wall_bedroom_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [1, 2],
         title: 'Cabeceira',
         subtitle: 'Suite',
         id: 'switch.switch_wall_bedroom_center',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [2, 2],
         title: 'Closet',
         subtitle: 'Suite',
         id: 'switch.switch_wall_closet_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [0, 3],
         title: 'Central',
         subtitle: 'Banheiro (Suite)',
         id: 'switch.switch_wall_bathroom_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
    ]
  },
  {
    width: 3,
    height: 4,
    items: [
      {
         position: [0, 1],
         title: 'Central',
         subtitle: 'Corredor',
         id: 'switch.switch_wall_hall_3_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [1, 1],
         title: 'Central',
         subtitle: 'Escritório',
         id: 'switch.switch_wall_laboratory_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [0, 2],
         title: 'Quarto (hospede 1)',
         id: 'switch.switch_wall_bedroom_guest_1_top',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
      {
         position: [1, 2],
         title: 'Quarto (hospede 2)',
         id: 'switch.switch_wall_bedroom_guest_2_left',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: null,
      },
    ]
  }
];
