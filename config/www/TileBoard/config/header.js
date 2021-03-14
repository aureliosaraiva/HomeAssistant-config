
var HEADER = { // https://github.com/resoai/TileBoard/wiki/Header-configuration
   styles: {
      margin: '30px 130px 30px 130px',
      fontSize: '28px'
   },
   right: [
     {
        type: HEADER_ITEMS.WEATHER,
        styles: {
           margin: '0 0 0'
        },
        icon: '&weather.casaenseada.state',
        icons: {
          'sunny': 'clear',
          'clear-night': 'clear',
          'clear-night': 'nt-clear',
          'cloudy': 'cloudy',
          'rainy': 'rain',
          'snowy': 'snow',
          'windy': 'hazy',
          'fog': 'fog',
          'partlycloudy': 'partlycloudy',
          'partlycloudy': 'nt-partlycloudy'
       },
        fields: {
           temperature: '&weather.casaenseada.attributes.temperature',
           temperatureUnit: '°C',
        }
     },
   ],
   left: [

      {
         type: HEADER_ITEMS.DATETIME,
         dateFormat: 'LLLL dd', //https://docs.angularjs.org/api/ng/filter/date
      }
   ]
}
