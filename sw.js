if(!self.define){let e,s={};const c=(c,i)=>(c=new URL(c+".js",i).href,s[c]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=c,e.onload=s,document.head.appendChild(e)}else e=c,importScripts(c),s()})).then((()=>{let e=s[c];if(!e)throw new Error(`Module ${c} didn’t register its module`);return e})));self.define=(i,a)=>{const f=e||("document"in self?document.currentScript.src:"")||location.href;if(s[f])return;let r={};const n=e=>c(e,f),d={module:{uri:f},exports:r,require:n};s[f]=Promise.all(i.map((e=>d[e]||n(e)))).then((e=>(a(...e),r)))}}define(["./workbox-330ce1d9"],(function(e){"use strict";e.setCacheNameDetails({prefix:"water-security-dl"}),self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"assets/contact-us.52fbffed.js",revision:"d86187b40efeee4974b8f5fcc8c2e433"},{url:"assets/ErrorNotFound.01b1b448.js",revision:"5a120d409611e600fdc61c14d7356957"},{url:"assets/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.fd84f88b.woff",revision:"3e1afe59fa075c9e04c436606b77f640"},{url:"assets/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.4a4dbc62.woff2",revision:"a4160421d2605545f69a4cd6cd642902"},{url:"assets/index.2b1bb6d9.css",revision:"190332a49b10f458ed987b6f04ce603b"},{url:"assets/index.9294d9d4.js",revision:"7ac9188fffc4621b193c5b1ae8b7d409"},{url:"assets/IndexPage.9e182f05.js",revision:"c15d9b7b630b2ef8af2eaa110988f9d3"},{url:"assets/KFOkCnqEu92Fr1MmgVxIIzQ.34e9582c.woff",revision:"4aa2e69855e3b83110a251c47fdd05fc"},{url:"assets/KFOlCnqEu92Fr1MmEU9fBBc-.9ce7f3ac.woff",revision:"40bcb2b8cc5ed94c4c21d06128e0e532"},{url:"assets/KFOlCnqEu92Fr1MmSU5fBBc-.bf14c7d7.woff",revision:"ea60988be8d6faebb4bc2a55b1f76e22"},{url:"assets/KFOlCnqEu92Fr1MmWUlfBBc-.e0fd57c0.woff",revision:"0774a8b7ca338dc1aba5a0ec8f2b9454"},{url:"assets/KFOlCnqEu92Fr1MmYUtfBBc-.f6537e32.woff",revision:"bcb7c7e2499a055f0e2f93203bdb282b"},{url:"assets/KFOmCnqEu92Fr1Mu4mxM.f2abf7fb.woff",revision:"d3907d0ccd03b1134c24d3bcaf05b698"},{url:"assets/LibraryPage.7ba2d6e1.js",revision:"785152cad25ecb43215942cb5b1ad11d"},{url:"assets/MainLayout.422c7f6a.css",revision:"00e96eabbcd03aee6bda9024b621ddd8"},{url:"assets/MainLayout.b5ca0009.js",revision:"e9a5f4564c118a10eaa3d8ec27c12eb9"},{url:"assets/map-WSNA.4a5cc700.png",revision:"babfe4932ecda4bd38ae892ca54cab8f"},{url:"assets/QPage.6f93c37f.js",revision:"b16118d694d7965d3be90e1a33b0e849"},{url:"assets/QSeparator.780ac445.js",revision:"b4419d7165b6ff8086e8f8ce98df4ee5"},{url:"assets/QSpinner.95ba3d24.js",revision:"3aa8de1931d852f6e609f8936191f981"},{url:"assets/render.1daacf64.js",revision:"abfe30206491edc709fefc2628c596dd"},{url:"assets/Ripple.334ef254.js",revision:"8145cdb1e3c5b3de5726fa109709cdb5"},{url:"assets/scroll.c7672006.js",revision:"14a55f4c7939af113d7389518cb2da47"},{url:"assets/use-size.af53fd94.js",revision:"ff7c115aa1febe6b529065b1a76bfa2f"},{url:"documents/13Or-Barber-2003-Technical_Report.pdf",revision:"3b5102d35ef81c5cc9e5a2725fe97a6e"},{url:"documents/14Or-Yoshikane-2006-Journal_Article.pdf",revision:"29f69c7466d4785d23fdce25879a0be0"},{url:"documents/17Da-Adams-2014-Journal_Article.pdf",revision:"2219c73bf682bf71226b5a7c894f241b"},{url:"documents/18Da-Adams-2016-Journal_Article.pdf",revision:"2ab8a4bdb92e7501ae835658f0bbc022"},{url:"documents/1Da-Wygralak-2006-Journal_Article.pdf",revision:"07e31450f1957eff06cda659906cc87a"},{url:"documents/27Da-Burrows-2012-Journal_Article.pdf",revision:"2996d8c06ad36fff80eec9f8e798e506"},{url:"documents/2Fi-Keryn-2015-Factsheet.pdf",revision:"435566f56c8c08d20c0e34efb92295e4"},{url:"documents/4Or-Doupé-2002-Journal_Article.pdf",revision:"32254f54d3ca90acf0424f20ed253a46"},{url:"documents/8Or-Payne-2004-Technical_Report.pdf",revision:"3e352e13e7501e51e8eb40f55d13256a"},{url:"favicon.ico",revision:"f4facfeaed834544d622544acfbb7722"},{url:"icons/apple-icon-120x120.png",revision:"d082235f6e6d2109e84e397f66fa868d"},{url:"icons/apple-icon-152x152.png",revision:"3c728ce3e709b7395be487becf76283a"},{url:"icons/apple-icon-167x167.png",revision:"3fec89672a18e4b402ede58646917c2d"},{url:"icons/apple-icon-180x180.png",revision:"aa47843bd47f34b7ca4b99f65dd25955"},{url:"icons/favicon-128x128.png",revision:"ab92df0270f054ca388127c9703a4911"},{url:"icons/favicon-16x16.png",revision:"e4b046d41e08e6fa06626d6410ab381d"},{url:"icons/favicon-32x32.png",revision:"410858b01fa6d3d66b7bf21447c5f1fc"},{url:"icons/favicon-96x96.png",revision:"db2bde7f824fb4057ffd1c42f6ed756e"},{url:"icons/icon-128x128.png",revision:"ab92df0270f054ca388127c9703a4911"},{url:"icons/icon-192x192.png",revision:"7659f0d3e9602e71811f8b7cf2ce0e8e"},{url:"icons/icon-256x256.png",revision:"cf5ad3498fb6fda43bdafd3c6ce9b824"},{url:"icons/icon-384x384.png",revision:"fdfc1b3612b6833a27a7b260c9990247"},{url:"icons/icon-512x512.png",revision:"2c2dc987945806196bd18cb6028d8bf4"},{url:"icons/ms-icon-144x144.png",revision:"8de1b0e67a62b881cd22d935f102a0e6"},{url:"icons/safari-pinned-tab.svg",revision:"3e4c3730b00c89591de9505efb73afd3"},{url:"images/pexels-pixabay-355700.jpg",revision:"ea5332c9074d3911f0c15c6ab97d7fd8"},{url:"index.html",revision:"86b22283680084fa322745735b84228d"},{url:"manifest.json",revision:"c5ae9bec8e679471133a86ff9890b528"}],{}),e.cleanupOutdatedCaches(),e.registerRoute(new e.NavigationRoute(e.createHandlerBoundToURL("index.html"),{denylist:[/sw\.js$/,/workbox-(.)*\.js$/]}))}));