if(!self.define){let e,c={};const i=(i,s)=>(i=new URL(i+".js",s).href,c[i]||new Promise((c=>{if("document"in self){const e=document.createElement("script");e.src=i,e.onload=c,document.head.appendChild(e)}else e=i,importScripts(i),c()})).then((()=>{let e=c[i];if(!e)throw new Error(`Module ${i} didn’t register its module`);return e})));self.define=(s,a)=>{const n=e||("document"in self?document.currentScript.src:"")||location.href;if(c[n])return;let r={};const d=e=>i(e,n),o={module:{uri:n},exports:r,require:d};c[n]=Promise.all(s.map((e=>o[e]||d(e)))).then((e=>(a(...e),r)))}}define(["./workbox-330ce1d9"],(function(e){"use strict";e.setCacheNameDetails({prefix:"water-security-dl"}),self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"assets/contact-us.3aa855c9.js",revision:"ccecd9cebe330e21dfd0e02246ad8d70"},{url:"assets/ErrorNotFound.6b3fadef.js",revision:"06dede555e07d6e21f737eef0155e7c4"},{url:"assets/flUhRq6tzZclQEJ-Vdg-IuiaDsNa.fd84f88b.woff",revision:"3e1afe59fa075c9e04c436606b77f640"},{url:"assets/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.4a4dbc62.woff2",revision:"a4160421d2605545f69a4cd6cd642902"},{url:"assets/index.2b1bb6d9.css",revision:"190332a49b10f458ed987b6f04ce603b"},{url:"assets/index.421eb415.js",revision:"e00368aea81efea618082e22652a934c"},{url:"assets/IndexPage.e1d5210d.js",revision:"e0ab96e787132eaddfac02082c525edc"},{url:"assets/KFOkCnqEu92Fr1MmgVxIIzQ.34e9582c.woff",revision:"4aa2e69855e3b83110a251c47fdd05fc"},{url:"assets/KFOlCnqEu92Fr1MmEU9fBBc-.9ce7f3ac.woff",revision:"40bcb2b8cc5ed94c4c21d06128e0e532"},{url:"assets/KFOlCnqEu92Fr1MmSU5fBBc-.bf14c7d7.woff",revision:"ea60988be8d6faebb4bc2a55b1f76e22"},{url:"assets/KFOlCnqEu92Fr1MmWUlfBBc-.e0fd57c0.woff",revision:"0774a8b7ca338dc1aba5a0ec8f2b9454"},{url:"assets/KFOlCnqEu92Fr1MmYUtfBBc-.f6537e32.woff",revision:"bcb7c7e2499a055f0e2f93203bdb282b"},{url:"assets/KFOmCnqEu92Fr1Mu4mxM.f2abf7fb.woff",revision:"d3907d0ccd03b1134c24d3bcaf05b698"},{url:"assets/LibraryPage.cb2d35da.js",revision:"f68c4e465f06030dc88d1a2d07668a40"},{url:"assets/MainLayout.09a63468.js",revision:"c2abc8d0c3b8c6c59096343fee495ad4"},{url:"assets/MainLayout.39d52476.css",revision:"8b2ddb3c2f2bae2660160210bf33bb8d"},{url:"assets/map-WSNA.4a5cc700.png",revision:"babfe4932ecda4bd38ae892ca54cab8f"},{url:"assets/QBtn.745f1236.js",revision:"2345a460d606c0b23e31ac838c7f0c53"},{url:"assets/QPage.fe582039.js",revision:"0407487d6aca76bbc65837d986cd4ef7"},{url:"assets/QSeparator.676edbf1.js",revision:"493c37e8e8b768dd674125f4c7e9cbf9"},{url:"assets/QSpinner.1a2858c5.js",revision:"c50402dff3b27e873d4e4077ca9351b4"},{url:"assets/render.95266ed8.js",revision:"0683f47c60d44848a447610484223f86"},{url:"assets/Ripple.fe56e056.js",revision:"8f65380405c5f3a6650ee632955ebe70"},{url:"assets/scroll.836e5675.js",revision:"dd5a2894be064f8dd5cfd9ce0f140b8c"},{url:"assets/use-size.7b96fa90.js",revision:"706625c39ca8ccddea21d3c16a78e4ad"},{url:"documents/0001Da-Wygralak-2006-Journal_Article.pdf",revision:"07e31450f1957eff06cda659906cc87a"},{url:"documents/0002Fi-Keryn-2015-Factsheet.pdf",revision:"435566f56c8c08d20c0e34efb92295e4"},{url:"documents/0004Or-Doupé-2002-Journal_Article.pdf",revision:"32254f54d3ca90acf0424f20ed253a46"},{url:"documents/0008Or-Payne-2004-Technical_Report.pdf",revision:"3e352e13e7501e51e8eb40f55d13256a"},{url:"documents/0013Or-Barber-2003-Technical_Report.pdf",revision:"3b5102d35ef81c5cc9e5a2725fe97a6e"},{url:"documents/0014Or-Yoshikane-2006-Journal_Article.pdf",revision:"29f69c7466d4785d23fdce25879a0be0"},{url:"documents/0017Da-Adams-2014-Journal_Article.pdf",revision:"2219c73bf682bf71226b5a7c894f241b"},{url:"documents/0018Da-Adams-2016-Journal_Article.pdf",revision:"2ab8a4bdb92e7501ae835658f0bbc022"},{url:"documents/0027Da-Burrows-2012-Journal_Article.pdf",revision:"2996d8c06ad36fff80eec9f8e798e506"},{url:"documents/0031Da-Cattarino-2018-Journal_Article.pdf",revision:"1b144d41ab422a87bac03728e2c86757"},{url:"favicon.ico",revision:"215b8dab7329df98bb819a4d107d0629"},{url:"icons/android-icon-144x144.png",revision:"9211cd680974b478aeea86084d0ef3bd"},{url:"icons/android-icon-192x192.png",revision:"577368e54b81cd151788b335b7a6463d"},{url:"icons/android-icon-36x36.png",revision:"026a2ea387b44bd5472ec80a1a1f9860"},{url:"icons/android-icon-48x48.png",revision:"20c713ca8dd18206d7e7766f374f59e1"},{url:"icons/android-icon-72x72.png",revision:"514cdcb327863976b86c33b3ecb69885"},{url:"icons/android-icon-96x96.png",revision:"db66fbd3ad040fd4d8ffbe80b8a70c7d"},{url:"icons/apple-icon-114x114.png",revision:"640a3f5d5ffc0ac2680fecc06b8dd246"},{url:"icons/apple-icon-120x120.png",revision:"64ef0a3ba0136d6960ca07a44970b2ef"},{url:"icons/apple-icon-144x144.png",revision:"9211cd680974b478aeea86084d0ef3bd"},{url:"icons/apple-icon-152x152.png",revision:"e0ce2004a3db5467c5db4faf8b1c7834"},{url:"icons/apple-icon-180x180.png",revision:"f49d0686863cc6079d642ec84a1e5fb9"},{url:"icons/apple-icon-57x57.png",revision:"30671471e78fa1798e1cd379403719ff"},{url:"icons/apple-icon-60x60.png",revision:"448a2b9a692feeeaa47f51ae07a0ea79"},{url:"icons/apple-icon-72x72.png",revision:"514cdcb327863976b86c33b3ecb69885"},{url:"icons/apple-icon-76x76.png",revision:"7bb9f94be478925faf61cee3c34f157c"},{url:"icons/apple-icon-precomposed.png",revision:"2fea3e78a37146aee22acd4c200e457d"},{url:"icons/apple-icon.png",revision:"2fea3e78a37146aee22acd4c200e457d"},{url:"icons/favicon-16x16.png",revision:"f2969f911bdb99a60404329283cf10b0"},{url:"icons/favicon-180x180.png",revision:"f49d0686863cc6079d642ec84a1e5fb9"},{url:"icons/favicon-32x32.png",revision:"faece6004868a72a97adfe0deb83597c"},{url:"icons/favicon-96x96.png",revision:"db66fbd3ad040fd4d8ffbe80b8a70c7d"},{url:"icons/favicon.ico",revision:"215b8dab7329df98bb819a4d107d0629"},{url:"icons/ms-icon-144x144.png",revision:"9211cd680974b478aeea86084d0ef3bd"},{url:"icons/ms-icon-150x150.png",revision:"2480b27da8ade043b379ed66cf01c2fc"},{url:"icons/ms-icon-310x310.png",revision:"e370994ae57034a227f3f27a916dd8a7"},{url:"icons/ms-icon-70x70.png",revision:"99d30bd801659160f9ae57359093e9c1"},{url:"images/charles-darwin-uni-logo.svg",revision:"f9bb3b7b4c7dfe68f346162ded1eda4d"},{url:"images/cqu-logo.png",revision:"315f4d8324160227d5025e900104a6e2"},{url:"images/header-image.jpg",revision:"3b5b47b5547afa2c7ef9e0b0fc777b1f"},{url:"images/JCU Logo - Horizontal RGB.png",revision:"9c58ce3d6eae436378401852d97c74d3"},{url:"index.html",revision:"b3b93948011de24e58ccc66076c3f84f"},{url:"manifest.json",revision:"c5ae9bec8e679471133a86ff9890b528"}],{}),e.cleanupOutdatedCaches(),e.registerRoute(new e.NavigationRoute(e.createHandlerBoundToURL("index.html"),{denylist:[/sw\.js$/,/workbox-(.)*\.js$/]}))}));
