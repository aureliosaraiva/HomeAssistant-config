var PANEL_LIVING_ROOM = [
  {
    width: 1,
    height: 4,
    title: 'Cenas',
    items: [
      {
         position: [0, 0],
         title: 'Modo filme',
         id: 'scene.light_movie_enable',
         type: TYPES.SCENE,
         state: false,
         icon: 'mdi-theater',
      }
    ]
  },
  {
    width: 5,
    height: 4,
    title: 'Luzes',
    items: [
      {
         position: [0, 0],
         title: 'Sala',
         id: 'light.lamps_living_room',
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
         colorpicker: true
       }
    ]
  },
];
