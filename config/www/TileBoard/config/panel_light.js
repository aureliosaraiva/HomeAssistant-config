var PANEL_LIGHT = [
  {
    width: 3,
    height: 4,
    items: [
      {
         position: [0, 1],
         title: 'Central',
         subtitle: 'Sala',
         id: 'light.lamps_center_livingroom',
         type: TYPES.LIGHT,
         states: {
            on: "On",
            off: "Off"
         },
         icons: {
            on: "mdi-lightbulb-on",
            off: "mdi-lightbulb",
         },
         sliders: [
            {
               title: 'Brightness',
               field: 'brightness',
               max: 255,
               min: 0,
               step: 5,
               request: {
                  type: "call_service",
                  domain: "light",
                  service: "turn_on",
                  field: "brightness"
               }
            },
            {
               title: 'Color temp',
               field: 'color_temp',
               max: 588,
               min: 153,
               step: 15,
               request: {
                  type: "call_service",
                  domain: "light",
                  service: "turn_on",
                  field: "color_temp"
               }
            }
         ],
      },
      {
         position: [1, 1],
         title: 'Arandela',
         subtitle: 'Sala',
         id: 'switch.switch_wall_garden_bottom',
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
         position: [2, 1],
         title: 'Central',
         subtitle: 'Hall',
         id: 'switch.switch_wall_hall_1_l2_hall',
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
         title: 'Central',
         subtitle: 'Cozinha',
         id: 'switch.switch_wall_kitchen_top',
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
         title: 'Central',
         subtitle: 'Lavanderia',
         id: 'switch.switch_wall_laundry_top',
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
      }
    ]
  },
  {
    width: 3,
    height: 4,
    items: [
      {
         position: [0, 1],
         title: 'Piscina',
         subtitle: 'Jardim',
         id: 'switch.switch_wall_garden_center',
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
         title: 'Varanda',
         subtitle: 'Jardim',
         id: 'switch.switch_wall_garden_top',
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
         title: 'Garagem',
         subtitle: 'Jardim',
         id: 'switch.switch_wall_hall_1_l1_garage',
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
         title: 'Hall Lavanderia',
         subtitle: 'Jardim',
         id: 'switch.switch_wall_laundry_center',
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
         position: [2, 1],
         title: 'Lateral',
         subtitle: 'Jardim',
         id: 'switch.switch_wall_hall_2_l3_external_side',
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

console.log('teste');
