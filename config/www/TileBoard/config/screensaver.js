var SCREENSAVER = {// optional. https://github.com/resoai/TileBoard/wiki/Screensaver-configuration
   timeout: 300, // after 5 mins of inactive
   slidesTimeout: 10, // 10s for one slide
   styles: { fontSize: '40px' },
   leftBottom: [{ type: SCREENSAVER_ITEMS.DATETIME }], // put datetime to the left-bottom of screensaver
   slides: [
      { bg: 'images/bg1.jpeg' },
      {
         bg: 'images/bg2.png',
         rightTop: [ // put text to the 2nd slide
            {
               type: SCREENSAVER_ITEMS.CUSTOM_HTML,
               html: 'Welcome to the <b>TileBoard</b>',
               styles: { fontSize: '40px' }
            }
         ]
      },
      { bg: 'images/bg3.jpg' }
   ]
};
