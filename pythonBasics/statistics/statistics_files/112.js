(window.__LOADABLE_LOADED_CHUNKS__=window.__LOADABLE_LOADED_CHUNKS__||[]).push([[112],{fLhW:function(t,e,n){"use strict";var o=n("tYyt"),r=n("fw5G"),a=n.n(r),i=n("eikI"),c=n("24Ii"),u=n.n(c),d=n("hFGM"),p=function canUseBeacon(){return window.navigator&&"function"==typeof window.navigator.sendBeacon},f=function sendBeacon(t,e){return navigator.sendBeacon(t,e)},s=function sendXHR(t,e){var n=u.a.post(t).use(d.b).use(d.c);e instanceof FormData||n.setHeader("Content-Type","text/plain;charset=UTF-8"),n.send(e).end()},l=function beacon(t,e){var n=arguments.length>2&&void 0!==arguments[2]&&arguments[2],o=!n&&p(),r=new a.a(t).addQueryParam("authentication_token",i.a.get("authentication_token")).toString();o?f(r,e):s(r,e)};function _objectWithoutProperties(t,e){if(null==t)return{};var n,o,r=function _objectWithoutPropertiesLoose(t,e){if(null==t)return{};var n,o,r={},a=Object.keys(t);for(o=0;o<a.length;o++)n=a[o],e.indexOf(n)>=0||(r[n]=t[n]);return r}(t,e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(t);for(o=0;o<a.length;o++)n=a[o],e.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(t,n)&&(r[n]=t[n])}return r}function _objectSpread(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{},o=Object.keys(Object(n));"function"==typeof Object.getOwnPropertySymbols&&(o=o.concat(Object.getOwnPropertySymbols(n).filter(function(t){return Object.getOwnPropertyDescriptor(n,t).enumerable}))),o.forEach(function(e){_defineProperty(t,e,n[e])})}return t}function _defineProperty(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}n.d(e,"b",function(){return v}),n.d(e,"c",function(){return h}),n.d(e,"e",function(){return w}),n.d(e,"f",function(){return _}),n.d(e,"d",function(){return g}),n.d(e,"a",function(){return y});var v=function track(t,e){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},r=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},a=r.gdprSafe,i=void 0!==a&&a;var c="";"undefined"!=typeof CCDATA&&"development"===CCDATA.env&&(c="http://".concat(window.location.hostname,":").concat(window.location.port)),c="".concat(c,"/events/").concat(t),n=_objectSpread({},n,{fullpath:n.fullpath||window.location.pathname+window.location.search,search:n.search||window.location.search,path:n.fullpath||window.location.pathname,title:n.title||window.document.title,url:n.url||window.location.href});var u=new FormData;u.append("category",t),u.append("event",e),u.append("properties",JSON.stringify(n)),u.append("authenticity_token",o.a.get("authenticity_token")),u.append("gdpr_safe","".concat(i)),l(c,u)},h=function trackContentItemEvent(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"user",e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"click",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},o=n.contentItem,r=_objectWithoutProperties(n,["contentItem"]);if(o){var a=o.type,i=o.progress;if(void 0===a||void 0===i)return;var c="quiz"===a,u=i.progress_percentage;c&&(u=i.passed?100:0),r=_objectSpread({up_next:o.upNext,content_item_progress:u,content_item_score:c?i.highest_percentage:null,content_item_type:a,quiz_retake:c&&i.taken},r)}r=_objectSpread({version:"v2_dashboard"},r),v(t,e,r)},w=function trackUserClick(t){v("user","click",t)},_=function trackUserVisit(t){v("user","visit",t)},g=function trackTabChangeEvent(t,e){return function(n){var o=e[n],r="".concat(t,"_").concat(o);w({target:r})}},y=function pushDataLayerEvent(t){void 0===window.dataLayer&&(window.dataLayer=[]),window.dataLayer.push({event:t})}}}]);
//# sourceMappingURL=112.f56f7d79aabb845d613c.chunk.js.map