(window.__LOADABLE_LOADED_CHUNKS__=window.__LOADABLE_LOADED_CHUNKS__||[]).push([[128],{lvaA:function(e,t,r){"use strict";var n=r("iOII"),o=r.n(n),a=r("1TcP"),c=r.n(a),i=r("q1tI"),u=r.n(i),l=r("W2rJ"),f=r.n(l),s=function getAttributeValue(e,t){var r=new RegExp("".concat(t,'="(.*?)"')),n=e.match(r);return n&&n[1]},b=function transformViewBox(e){var t=s(e,"width"),r=s(e,"height");return r&&t?e.replace(/width=".*?" ?/,"").replace(/height=".*?" ?/,"").replace("<svg",'<svg viewBox="0 0 '.concat(parseInt(t,10)," ").concat(parseInt(r,10),'"')):e};function _extends(){return(_extends=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e}).apply(this,arguments)}function _slicedToArray(e,t){return function _arrayWithHoles(e){if(Array.isArray(e))return e}(e)||function _iterableToArrayLimit(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var r=[],n=!0,o=!1,a=void 0;try{for(var c,i=e[Symbol.iterator]();!(n=(c=i.next()).done)&&(r.push(c.value),!t||r.length!==t);n=!0);}catch(e){o=!0,a=e}finally{try{n||null==i.return||i.return()}finally{if(o)throw a}}return r}(e,t)||function _nonIterableRest(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function _defineProperty(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}t.a=function SafeSvg(e){var t=e.src,r=e.fallback,n=e.title,a=e.svgProps,l=e.viewBox,s=function _objectSpread(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{},n=Object.keys(Object(r));"function"==typeof Object.getOwnPropertySymbols&&(n=n.concat(Object.getOwnPropertySymbols(r).filter(function(e){return Object.getOwnPropertyDescriptor(r,e).enumerable}))),n.forEach(function(t){_defineProperty(e,t,r[t])})}return e}({cacheRequests:!1,title:n},a),p=_slicedToArray(Object(i.useState)(t),2),y=p[0],v=p[1],_=Object(i.useCallback)(function(){return v(r)},[r]),O=Object(i.useMemo)(function(){var e=[l&&b,c.a].filter(o.a);return function(t){return e.reduce(function(e,t){return t(e)},t)}},[l]);return u.a.createElement(f.a,_extends({src:y,onError:_,preProcessor:O},s))}}}]);
//# sourceMappingURL=128.ae68757af0fd8737c0b7.chunk.js.map