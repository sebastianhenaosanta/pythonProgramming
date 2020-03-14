(window.__LOADABLE_LOADED_CHUNKS__=window.__LOADABLE_LOADED_CHUNKS__||[]).push([[100],{"4OwO":function(e,t,r){e.exports={fileNameInput:"fileNameInput__2GfLF62PzEHPiitohhIKyM",createItemForm:"createItemForm__2lX6_UQqFgblvZnKq59CTe",addItemControlEnabled:"addItemControlEnabled__1-PLEXW9T7UWPtMir8mTAE"}},D5Q1:function(e,t,r){"use strict";var o=r("o0o1"),n=r.n(o),a=r("4qC0"),i=r.n(a),l=r("q1tI"),s=r.n(l),c=r("33yf"),p=r.n(c),u=r("TSYQ"),f=r.n(u),d=r("uBVh"),m=r("b+vN"),h=r("uM7l"),y=r.n(h),_=r("i8i4"),v=r.n(_),g=r("Hutj"),b=r("NuJE"),F=r("y3J+"),w=r("zeeO"),O=r.n(w);function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function _defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function _possibleConstructorReturn(e,t){return!t||"object"!==_typeof(t)&&"function"!=typeof t?function _assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function _getPrototypeOf(e){return(_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function _setPrototypeOf(e,t){return(_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var T=function(e){function FileTreeItem(){var e,t;!function _classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,FileTreeItem);for(var r=arguments.length,o=new Array(r),n=0;n<r;n++)o[n]=arguments[n];return(t=_possibleConstructorReturn(this,(e=_getPrototypeOf(FileTreeItem)).call.apply(e,[this].concat(o)))).state={name:t.props.name,hover:!1,isRenaming:!1,toggleMenuOption:!1},t.onFileNameChange=function(e){t.setState({name:e.target.value}),t.props.clearError()},t.resetName=function(){t.setState({name:t.props.name})},t.forceFocus=function(){v.a.findDOMNode(t.refs.nameInput).focus(),v.a.findDOMNode(t.refs.nameInput).select(),t.props.setCurrentFile(t.props.path,!0)},t.handleClick=function(e){t.props.clearError(),e.stopPropagation(),t.disabledItem()||t.state.isRenaming||(t.props.folder&&t.props.handleClick(),t.props.setCurrentItem(t.props.path,t.props.folder))},t.triggerNameChange=function(e){if(e&&e.preventDefault(),t.props.name!==t.state.name){var r=t.props.path,o=y()(r);o=o.replace(t.props.name,t.state.name),t.props.renameFile(r,o)}t.setState({isRenaming:!1})},t.onMouseEnter=function(){t.setState({hover:!0})},t.onMouseLeave=function(){t.setState({hover:!1})},t.disabledItem=function(){return!t.props.default&&(["binary"].includes(t.props.type)||t.props.disabled)},t.renderItemName=function(){if(t.state.isRenaming)return s.a.createElement("form",{onSubmit:t.triggerNameChange,className:O.a.renameForm},s.a.createElement("input",{ref:"nameInput",className:O.a.renameFormInput,value:t.state.name,onChange:t.onFileNameChange,onBlur:t.triggerNameChange}));var e=t.props.default?" (Default)":"";return s.a.createElement("span",{className:O.a.itemName},"".concat(t.props.name).concat(e))},t.handleEditClick=function(){t.refs.dropdown.close(),t.setState({isRenaming:!0,name:t.props.name},function(){t.forceFocus()})},t.handleDeleteClick=function(){t.refs.dropdown.close(),t.props.setCurrentItem(t.props.path,t.props.folder,t.disabledItem()),t.props.getDeleteConfirmation(t.props.path)},t.handleNewFolder=function(){t.refs.dropdown.close(),t.handleNewItem(!0)},t.handleNewFile=function(){t.refs.dropdown.close(),t.handleNewItem()},t.handleNewItem=function(e){t.props.setCurrentItem(t.props.path,t.props.folder),t.props.forceAddOpenPath(t.props.path),t.setState({remainOpen:!0},function(){e?t.props.handleNewFolder():t.props.handleNewFile()})},t.handleDropdown=function(e){e.stopPropagation()},t.renderMenu=function(){var e=t.props.folder?"Delete Folder":"Delete File";return s.a.createElement(b.a,{column:!0,className:O.a.dropdown},t.props.folder?s.a.createElement("button",{className:O.a.dropdownOption,onClick:t.handleNewFile,"data-testid":"add-file-".concat(t.props.name),type:"button"},"New File"):null,t.props.folder?s.a.createElement("button",{className:O.a.dropdownOption,onClick:t.handleNewFolder,"data-testid":"add-folder-".concat(t.props.name),type:"button"},"New Folder"):null,t.props.isRoot?null:s.a.createElement("button",{className:O.a.dropdownOption,onClick:t.handleEditClick,"data-testid":"rename-item-".concat(t.props.name),type:"button"},"Rename"),t.props.isRoot?null:s.a.createElement("button",{className:O.a.dropdownOption,onClick:t.handleDeleteClick,"data-testid":"delete-item-".concat(t.props.name),type:"button"},e))},t.handleDropDownToggle=function(e){t.setState(function(){return{toggleMenuOption:e,hover:e}})},t}return function _inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&_setPrototypeOf(e,t)}(FileTreeItem,s.a.Component),function _createClass(e,t,r){return t&&_defineProperties(e.prototype,t),r&&_defineProperties(e,r),e}(FileTreeItem,[{key:"render",value:function render(){var e=this.props.isRoot?3:15*this.props.nestCount,t=f()({[O.a.fileTreeTreeBtn]:!0,[O.a.fileTreeTreeBtnActive]:this.props.currentItemPath===this.props.path,[O.a.fileTreeTreeBtnInactive]:this.disabledItem()}),r=this.state.hover&&!this.state.isRenaming||this.state.toggleMenuOption,o=this.props.isOpen?"arrow-filled-down":"arrow-filled-right",n=this.props.folder?s.a.createElement(g.a,{className:O.a.folderItem,name:"folder-filled"}):null,a=s.a.createElement(g.a,{className:O.a.icon,title:"Options",name:"in-progress"});return s.a.createElement("div",{"data-testid":"file-nav-item-".concat(this.props.name)},s.a.createElement("div",{title:this.props.name,className:t,style:{paddingLeft:e},onClick:this.handleClick,onMouseEnter:this.onMouseEnter,onMouseLeave:this.onMouseLeave,"data-testid":"file-nav-title-".concat(this.props.name)},this.props.folder?s.a.createElement(g.a,{name:o}):null,this.props.isRoot?null:n,this.renderItemName(),r?s.a.createElement("div",{className:O.a.rightIcons,onClick:this.handleDropdown,"data-testid":"file-nav-item-opts-".concat(this.props.name)},s.a.createElement(F.a,{ref:"dropdown",clickTarget:a,onToggle:this.handleDropDownToggle,popoverOffset:2},this.renderMenu())):null),this.props.isOpen?this.props.children:null)}}]),FileTreeItem}(),P=r("yzbm"),N=r("iPqP"),C=r.n(N),I=function readUploadedFile(e,t){var r=new FileReader;return new Promise(function(o,n){r.onerror=function(){r.abort(),n(new DOMException("Problem parsing input file."))},r.onprogress=function(e){t(e)},r.onload=function(){var e=r.result;o(e.split(",")[1])},r.readAsDataURL(e)})};function _extends(){return(_extends=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var o in r)Object.prototype.hasOwnProperty.call(r,o)&&(e[o]=r[o])}return e}).apply(this,arguments)}function _defineProperty(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function asyncGeneratorStep(e,t,r,o,n,a,i){try{var l=e[a](i),s=l.value}catch(e){return void r(e)}l.done?t(s):Promise.resolve(s).then(o,n)}function _asyncToGenerator(e){return function(){var t=this,r=arguments;return new Promise(function(o,n){var a=e.apply(t,r);function _next(e){asyncGeneratorStep(a,o,n,_next,_throw,"next",e)}function _throw(e){asyncGeneratorStep(a,o,n,_next,_throw,"throw",e)}_next(void 0)})}}var E=function(){var e=_asyncToGenerator(n.a.mark(function _callee(e,t){var r;return n.a.wrap(function _callee$(o){for(;;)switch(o.prev=o.next){case 0:return o.prev=0,o.next=3,I(e,t);case 3:return r=o.sent,o.abrupt("return",[e,r,null]);case 7:return o.prev=7,o.t0=o.catch(0),o.abrupt("return",[e,"",o.t0]);case 10:case"end":return o.stop()}},_callee,this,[[0,7]])}));return function fetchFileContents(t,r){return e.apply(this,arguments)}}(),S=function FileDropzone(e){var t=e.children,r=e.className,o=e.dragActiveClassName,a=void 0===o?C.a.dragActive:o,i=e.onFileUpload,c=e.dropzoneOptions,p=e.testId,u=void 0===p?"file-dropzone":p,d=e.onProgress,m=void 0===d?function(){}:d,h=Object(l.useCallback)(function(){var e=_asyncToGenerator(n.a.mark(function _callee2(e,t){var r,o;return n.a.wrap(function _callee2$(n){for(;;)switch(n.prev=n.next){case 0:return r=e.map(function(e){return E(e,m)}),n.next=3,Promise.all(r);case 3:o=n.sent,i({files:o,rejectedFiles:t});case 5:case"end":return n.stop()}},_callee2,this)}));return function(t,r){return e.apply(this,arguments)}}(),[i,m]),y=Object(P.a)(function _objectSpread(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{},o=Object.keys(Object(r));"function"==typeof Object.getOwnPropertySymbols&&(o=o.concat(Object.getOwnPropertySymbols(r).filter(function(e){return Object.getOwnPropertyDescriptor(r,e).enumerable}))),o.forEach(function(t){_defineProperty(e,t,r[t])})}return e}({noDragEventsBubbling:!0,multiple:!0,maxSize:3e7,onDrop:h},c)),_=y.getRootProps,v=y.getInputProps,g=y.isDragActive,b=s.a.createElement("input",v());return s.a.createElement("div",_extends({"data-testid":u},_(),{className:f()({[a]:g},C.a.fileDropzone,r)}),b,t)},A=r("RpHP"),j=r.n(A);function FileTree_typeof(e){return(FileTree_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function FileTree_defineProperty(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function FileTree_defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function FileTree_possibleConstructorReturn(e,t){return!t||"object"!==FileTree_typeof(t)&&"function"!=typeof t?function FileTree_assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function FileTree_getPrototypeOf(e){return(FileTree_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function FileTree_setPrototypeOf(e,t){return(FileTree_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var k=function(e){function FileTree(){var e,t;!function FileTree_classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,FileTree);for(var r=arguments.length,o=new Array(r),n=0;n<r;n++)o[n]=arguments[n];return(t=FileTree_possibleConstructorReturn(this,(e=FileTree_getPrototypeOf(FileTree)).call.apply(e,[this].concat(o)))).writeItem=function(e,r){if(!d.d(e.name))return s.a.createElement(T,{type:e.type,path:e.path,key:e.path,name:e.name,default:t.props.defaultFile===e.path,disabled:t.props.disabled||d.c(e.name),setError:t.props.setError,renameFile:t.props.renameFile,clearError:t.props.clearError,setCurrentFile:t.setCurrentFile,setCurrentItem:t.props.setCurrentItem,currentItemPath:t.props.currentItemPath,nestCount:r,getDeleteConfirmation:t.props.getDeleteConfirmation})},t.handleClick=function(){t.props.setCurrentItem("",!0)},t.setCurrentFile=function(e,r){t.props.clearError(),t.props.setCurrentItem(e,r)},t.writeFolderItem=function(e,r){if(!d.d(e.name)){var o=e.name,n=e.path,a=t.props.openPaths.has(n);return s.a.createElement(T,{folder:!0,path:n,key:n,name:o,disabled:t.props.disabled,setError:t.props.setError,clearError:t.props.clearError,setCurrentItem:t.props.setCurrentItem,setCurrentFile:t.setCurrentFile,currentItemPath:t.props.currentItemPath,renameFile:t.props.renameFile,isOpen:a,nestCount:r,getDeleteConfirmation:t.props.getDeleteConfirmation,handleNewFolder:t.props.handleNewFolder,handleNewFile:t.props.handleNewFile,forceAddOpenPath:t.props.forceAddOpenPath,handleClick:function handleClick(){return t.props.addOrRemoveOpenPath(n)}},t.buildTree(e,r+1))}},t.buildTree=function(e,r){var o=[],n=!0,a=!1,i=void 0;try{for(var l,s=e.directories[Symbol.iterator]();!(n=(l=s.next()).done);n=!0){var c=l.value;o.push(t.writeFolderItem(c,r))}}catch(e){a=!0,i=e}finally{try{n||null==s.return||s.return()}finally{if(a)throw i}}var p=!0,u=!1,f=void 0;try{for(var d,m=e.files[Symbol.iterator]();!(p=(d=m.next()).done);p=!0){var h=d.value;o.push(t.writeItem(h,r))}}catch(e){u=!0,f=e}finally{try{p||null==m.return||m.return()}finally{if(u)throw f}}return o},t}return function FileTree_inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&FileTree_setPrototypeOf(e,t)}(FileTree,s.a.Component),function FileTree_createClass(e,t,r){return t&&FileTree_defineProperties(e.prototype,t),r&&FileTree_defineProperties(e,r),e}(FileTree,[{key:"render",value:function render(){var e=function FileTree_objectSpread(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{},o=Object.keys(Object(r));"function"==typeof Object.getOwnPropertySymbols&&(o=o.concat(Object.getOwnPropertySymbols(r).filter(function(e){return Object.getOwnPropertyDescriptor(r,e).enumerable}))),o.forEach(function(t){FileTree_defineProperty(e,t,r[t])})}return e}({files:[],directories:[]},this.props.workspaceRoot,{path:"",name:"files"});return s.a.createElement("div",{className:j.a.fileTree,onClick:this.handleClick},s.a.createElement(S,{dropzoneOptions:{noClick:!0},onFileUpload:this.props.handleFileUpload,onProgress:this.props.handleUploadProgress},this.writeFolderItem(e,0)))}}]),FileTree}(),x=r("XVAG"),D=r("2TUT"),R=r("MjJq"),M=r("ZDtF"),G=r("4OwO"),U=r.n(G);function FileToolInput_typeof(e){return(FileToolInput_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function FileToolInput_defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function FileToolInput_possibleConstructorReturn(e,t){return!t||"object"!==FileToolInput_typeof(t)&&"function"!=typeof t?function FileToolInput_assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function FileToolInput_getPrototypeOf(e){return(FileToolInput_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function FileToolInput_setPrototypeOf(e,t){return(FileToolInput_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var z=function(e){function FileToolInput(){var e,t;!function FileToolInput_classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,FileToolInput);for(var r=arguments.length,o=new Array(r),n=0;n<r;n++)o[n]=arguments[n];return(t=FileToolInput_possibleConstructorReturn(this,(e=FileToolInput_getPrototypeOf(FileToolInput)).call.apply(e,[this].concat(o)))).state={value:""},t.setFocus=function(){v.a.findDOMNode(t.refs.filenameinput).focus()},t.clearInput=function(){t.setState({value:""})},t.fileNameKeyDown=function(e){var r=e.target.value;t.setState({value:r}),t.props.fileNameKeyDown(r)},t.canAddItem=function(){return!t.props.hasError()&&""!==t.state.value},t.onAddItemClick=function(e){t.canAddItem()?t.props.onSubmit(e):t.props.toggle()},t}return function FileToolInput_inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&FileToolInput_setPrototypeOf(e,t)}(FileToolInput,s.a.Component),function FileToolInput_createClass(e,t,r){return t&&FileToolInput_defineProperties(e.prototype,t),r&&FileToolInput_defineProperties(e,r),e}(FileToolInput,[{key:"componentDidMount",value:function componentDidMount(){this.setFocus()}},{key:"render",value:function render(){var e=this.state.value,t=f()({[U.a.addItemControlEnabled]:this.canAddItem()}),r=this.canAddItem()?"plus":"close";return s.a.createElement("form",{onSubmit:this.props.onSubmit,className:U.a.createItemForm},s.a.createElement("input",{type:"text",className:U.a.fileNameInput,ref:"filenameinput",placeholder:this.props.placeHolder,value:e,onChange:this.fileNameKeyDown,"data-testid":"file-name-input"}),s.a.createElement("div",{className:t},s.a.createElement(x.a,{className:t,name:r,onClick:this.onAddItemClick,"data-testid":"file-name-input-".concat(r)})))}}]),FileToolInput}(),B=r("MKcU"),L=r.n(B);function NewFileTool_typeof(e){return(NewFileTool_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function NewFileTool_defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function NewFileTool_possibleConstructorReturn(e,t){return!t||"object"!==NewFileTool_typeof(t)&&"function"!=typeof t?function NewFileTool_assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function NewFileTool_getPrototypeOf(e){return(NewFileTool_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function NewFileTool_setPrototypeOf(e,t){return(NewFileTool_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var H=function(e){function NewFileTool(){var e,t;!function NewFileTool_classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,NewFileTool);for(var r=arguments.length,o=new Array(r),n=0;n<r;n++)o[n]=arguments[n];return(t=NewFileTool_possibleConstructorReturn(this,(e=NewFileTool_getPrototypeOf(NewFileTool)).call.apply(e,[this].concat(o)))).state={name:""},t.onSubmit=function(e){e.preventDefault(),t.createNewFileSystemItem()},t.reset=function(){t.props.reset(),t.setState({name:""})},t.fileNameKeyDown=function(e){t.setState({name:e}),t.props.clearError()},t.toggleLayout=function(){t.props.isAddingItem&&t.props.toggleAddItem(),t.props.toggle()},t.hasErrors=function(){return Boolean(t.props.error)},t.createNewFileSystemItem=function(){var e=t.props.isDir;t.props.createNewFileSystemItem(t.state.name,e).then(function(){t.hasErrors()||(t.props.toggleAddItem(),t.reset())})},t}return function NewFileTool_inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&NewFileTool_setPrototypeOf(e,t)}(NewFileTool,s.a.Component),function NewFileTool_createClass(e,t,r){return t&&NewFileTool_defineProperties(e.prototype,t),r&&NewFileTool_defineProperties(e,r),e}(NewFileTool,[{key:"render",value:function render(){var e=this.props.isDir?"Enter Folder Name":"Enter File Name",t=this.props.toolOpen?"close":"folder";return s.a.createElement("div",null,s.a.createElement("div",{className:L.a.fcnCreateFileTool},s.a.createElement("div",{className:L.a.fileToolMenu},this.props.toggle&&s.a.createElement(x.a,{"data-testid":"file-nav-expand",name:t,onClick:this.toggleLayout}),s.a.createElement("div",{className:L.a.toolsRight},s.a.createElement(S,{testId:"new-file-upload",className:L.a.fileUpload,dropzoneOptions:{noDrag:!0},onFileUpload:this.props.handleFileUpload,onProgress:this.props.handleUploadProgress},s.a.createElement(x.a,null,s.a.createElement(D.a,{title:"Upload a file"}))),s.a.createElement(x.a,null,s.a.createElement(R.a,{onClick:this.props.handleNewFolder,title:"Create a folder","data-testid":"add-folder"})),s.a.createElement(x.a,null,s.a.createElement(M.a,{onClick:this.props.handleNewFile,title:"Create a file","data-testid":"add-file"}))))),this.props.isAddingItem?s.a.createElement(z,{ref:"fileInput",toggle:this.props.toggleAddItem,hasError:this.hasErrors,placeHolder:e,fileNameKeyDown:this.fileNameKeyDown,onSubmit:this.onSubmit}):void 0)}}]),NewFileTool}(),K=r("/FR9"),q=r("4Te6"),Q=r("swBZ"),W=r("AW55"),J=r("volc"),Y=r.n(J);function FileNavigator_typeof(e){return(FileNavigator_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function _slicedToArray(e,t){return function _arrayWithHoles(e){if(Array.isArray(e))return e}(e)||function _iterableToArrayLimit(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var r=[],o=!0,n=!1,a=void 0;try{for(var i,l=e[Symbol.iterator]();!(o=(i=l.next()).done)&&(r.push(i.value),!t||r.length!==t);o=!0);}catch(e){n=!0,a=e}finally{try{o||null==l.return||l.return()}finally{if(n)throw a}}return r}(e,t)||function _nonIterableRest(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}function FileNavigator_asyncGeneratorStep(e,t,r,o,n,a,i){try{var l=e[a](i),s=l.value}catch(e){return void r(e)}l.done?t(s):Promise.resolve(s).then(o,n)}function FileNavigator_asyncToGenerator(e){return function(){var t=this,r=arguments;return new Promise(function(o,n){var a=e.apply(t,r);function _next(e){FileNavigator_asyncGeneratorStep(a,o,n,_next,_throw,"next",e)}function _throw(e){FileNavigator_asyncGeneratorStep(a,o,n,_next,_throw,"throw",e)}_next(void 0)})}}function FileNavigator_defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function FileNavigator_possibleConstructorReturn(e,t){return!t||"object"!==FileNavigator_typeof(t)&&"function"!=typeof t?function FileNavigator_assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function FileNavigator_getPrototypeOf(e){return(FileNavigator_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function FileNavigator_setPrototypeOf(e,t){return(FileNavigator_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var V=function(e){function FileNavigator(){var e,t;!function FileNavigator_classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,FileNavigator);for(var r=arguments.length,o=new Array(r),a=0;a<r;a++)o[a]=arguments[a];return(t=FileNavigator_possibleConstructorReturn(this,(e=FileNavigator_getPrototypeOf(FileNavigator)).call.apply(e,[this].concat(o)))).state={error:void 0,currentItemPath:"",currentSavePath:void 0,isAddingItem:!1,openPaths:new Set([""]),confirm:!1,isDir:!1},t.setCurrentItem=function(e,r,o){r?t.setState({currentSavePath:e}):(t.setState({currentSavePath:void 0}),t.state.currentItemPath===e||o||t.props.openFile(e)),t.setState({currentItemPath:e})},t.addOrRemoveOpenPath=function(e){var r=t.state.openPaths,o=new Set(r);o.has(e)?o.delete(e):o.add(e),t.setState({openPaths:o})},t.forceAddOpenPath=function(e){t.state.openPaths.has(e)||t.addOrRemoveOpenPath(e)},t.toggleAddFileState=function(){t.setState(function(e){return{isAddingItem:!e.isAddingItem}})},t.handleFileUpload=function(){var e=FileNavigator_asyncToGenerator(n.a.mark(function _callee(e){var r,o,a,i,l;return n.a.wrap(function _callee$(n){for(;;)switch(n.prev=n.next){case 0:return r=e.files,o=void 0===r?[]:r,a=e.rejectedFiles,i=o.map(function(e){var t=_slicedToArray(e,3),r=t[0],o=t[1];if(t[2])return null;var n=r.path?r.path.replace(/^\//,""):r.name;return new q.a({path:n,encodedContent:o,mimeType:r.type,name:r.name})}).filter(Boolean),l=i.map(function(e){var t=p.a.dirname(e.path);return t?new K.a({path:t,name:p.a.basename(t)}):null}).filter(Boolean),n.prev=3,n.next=6,t.props.createDirectories(l);case 6:n.next=11;break;case 8:n.prev=8,n.t0=n.catch(3),t.setError(n.t0);case 11:return n.prev=11,n.next=14,t.props.updateFiles(i);case 14:W.a.increment("learning_environment.files_uploaded","success"),n.next=20;break;case 17:n.prev=17,n.t1=n.catch(11),t.setError(n.t1);case 20:a&&a.length&&t.setError("\n        Rejected these files because they were too large:\n        ".concat(a.map(function(e){return" ".concat(e.name,", ")}),"\n      "));case 21:case"end":return n.stop()}},_callee,this,[[3,8],[11,17]])}));return function(t){return e.apply(this,arguments)}}(),t.createNewFileSystemItem=function(){var e=FileNavigator_asyncToGenerator(n.a.mark(function _callee2(e,r){var o,a,i,l;return n.a.wrap(function _callee2$(n){for(;;)switch(n.prev=n.next){case 0:if(!Object(d.c)(e)){n.next=3;break}return t.setError("Cannot create a file with this name and extension."),n.abrupt("return");case 3:if(t.setState({isAddingItem:!0}),o=t.state.currentSavePath?"".concat(t.state.currentSavePath,"/").concat(e):e,a=function onCreateSuccess(){t.setCurrentItem(o,r),t.forceAddOpenPath(o)},!r){n.next=12;break}return i=new K.a({name:e,path:o,files:[],directories:[]}),n.next=10,t.createDirectory(i,a);case 10:n.next=15;break;case 12:return l=new q.a({name:e,path:o,content:""}),n.next=15,t.createFile(l,a);case 15:case"end":return n.stop()}},_callee2,this)}));return function(t,r){return e.apply(this,arguments)}}(),t.createDirectory=function(){var e=FileNavigator_asyncToGenerator(n.a.mark(function _callee3(e,r){return n.a.wrap(function _callee3$(o){for(;;)switch(o.prev=o.next){case 0:return o.prev=0,o.next=3,t.props.createDirectories([e]);case 3:r(),o.next=9;break;case 6:o.prev=6,o.t0=o.catch(0),t.setError(o.t0);case 9:case"end":return o.stop()}},_callee3,this,[[0,6]])}));return function(t,r){return e.apply(this,arguments)}}(),t.createFile=function(){var e=FileNavigator_asyncToGenerator(n.a.mark(function _callee4(e,r){return n.a.wrap(function _callee4$(o){for(;;)switch(o.prev=o.next){case 0:return o.prev=0,o.next=3,t.props.updateFiles([e]);case 3:r(),o.next=9;break;case 6:o.prev=6,o.t0=o.catch(0),t.setError(o.t0);case 9:case"end":return o.stop()}},_callee4,this,[[0,6]])}));return function(t,r){return e.apply(this,arguments)}}(),t.handleRenameFile=function(){var e=FileNavigator_asyncToGenerator(n.a.mark(function _callee5(e,r){return n.a.wrap(function _callee5$(o){for(;;)switch(o.prev=o.next){case 0:return o.prev=0,o.next=3,t.props.renameFile(e,r);case 3:o.next=8;break;case 5:o.prev=5,o.t0=o.catch(0),t.setError(o.t0);case 8:case"end":return o.stop()}},_callee5,this,[[0,5]])}));return function(t,r){return e.apply(this,arguments)}}(),t.setError=function(e){i()(e)&&t.setState({error:e})},t.clearError=function(){t.setState({error:void 0})},t.getDeleteConfirmation=function(){t.setState({confirm:!0})},t.deleteFile=FileNavigator_asyncToGenerator(n.a.mark(function _callee6(){var e;return n.a.wrap(function _callee6$(r){for(;;)switch(r.prev=r.next){case 0:return e=t.state.currentItemPath,t.setState({confirm:!1}),r.prev=2,r.next=5,t.props.deleteFile(e);case 5:r.next=10;break;case 7:r.prev=7,r.t0=r.catch(2),t.setError(r.t0);case 10:t.setState({currentSavePath:"",currentItemPath:""});case 11:case"end":return r.stop()}},_callee6,this,[[2,7]])})),t.cancelAndClose=function(){t.setState({confirm:!1})},t.toggleAddFolder=function(){t.toggleAddItem(!0)},t.toggleAddFile=function(){t.toggleAddItem(!1)},t.toggleAddItem=function(e){t.clearError(),t.setState({isDir:e}),t.toggleAddFileState()},t.reset=function(){t.setState({isDir:!1,isAddingItem:!1})},t}return function FileNavigator_inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&FileNavigator_setPrototypeOf(e,t)}(FileNavigator,l["Component"]),function FileNavigator_createClass(e,t,r){return t&&FileNavigator_defineProperties(e.prototype,t),r&&FileNavigator_defineProperties(e,r),e}(FileNavigator,[{key:"render",value:function render(){var e=this.props.directory,t=void 0===e?{directories:[],files:[]}:e,r=f()({[Y.a.fileTool]:!0,[Y.a.fileToolIsAdding]:this.state.isAddingItem,[Y.a.fileToolClosed]:!this.props.open},this.props.className);return s.a.createElement("div",{className:r,"data-testid":"file-navigator"},s.a.createElement("div",{className:Y.a.fileToolContainer},this.state.error&&s.a.createElement("p",{className:Y.a.fileToolError},this.state.error),s.a.createElement(H,{toolOpen:this.props.open,toggle:this.props.toggleLayout,error:this.state.error,clearError:this.clearError,createNewFileSystemItem:this.createNewFileSystemItem,isAddingItem:this.state.isAddingItem,reset:this.reset,toggleAddItem:this.toggleAddItem,handleFileUpload:this.handleFileUpload,handleNewFile:this.toggleAddFile,handleNewFolder:this.toggleAddFolder,isDir:this.state.isDir}),this.props.open?s.a.createElement(k,{workspaceRoot:t,setCurrentItem:this.setCurrentItem,disabled:this.state.isAddingItem,defaultFile:this.props.defaultFile,setError:this.setError,clearError:this.clearError,currentItemPath:this.state.currentItemPath,addOrRemoveOpenPath:this.addOrRemoveOpenPath,forceAddOpenPath:this.forceAddOpenPath,getDeleteConfirmation:this.getDeleteConfirmation,handleNewFile:this.toggleAddFile,handleNewFolder:this.toggleAddFolder,handleFileUpload:this.handleFileUpload,openPaths:this.state.openPaths,renameFile:this.handleRenameFile}):null,s.a.createElement(m.a,{isOpen:this.state.confirm,action:this.deleteFile,cancel:this.cancelAndClose},s.a.createElement("div",null,s.a.createElement("h5",null,Q.components.confirmation_wall.delete_item),s.a.createElement("p",null,Q.components.confirmation_wall.cannot_undo))),this.props.controls))}}]),FileNavigator}();t.a=V},MKcU:function(e,t,r){e.exports={fcnCreateFileTool:"fcnCreateFileTool__1z1wtz_c7RhY2SEfseSEjL",fileToolMenu:"fileToolMenu__3lV0s5WgX4TDRnzCp8JfTO",toolsRight:"toolsRight__3OB2cC73sCf29c0F11ajJA",fileUpload:"fileUpload__17L-Zl9cNjz3487GiX02Co"}},QKYg:function(e,t,r){e.exports={dialogButton:"dialogButton__3GWCelmXvJ-RrkoiQmGr5x"}},RpHP:function(e,t,r){e.exports={fileTree:"fileTree__1bw3Dp6A-Ge88pVGbwFcYQ"}},"b+vN":function(e,t,r){"use strict";var o=r("q1tI"),n=r.n(o),a=r("MLxE"),i=r("QqFe"),l=r("NuJE"),s=r("TSYQ"),c=r.n(s),p=r("rtHi"),u=r("QKYg"),f=r.n(u);function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function _typeof(e){return typeof e}:function _typeof(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function _defineProperties(e,t){for(var r=0;r<t.length;r++){var o=t[r];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}function _possibleConstructorReturn(e,t){return!t||"object"!==_typeof(t)&&"function"!=typeof t?function _assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(e):t}function _getPrototypeOf(e){return(_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function _getPrototypeOf(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function _setPrototypeOf(e,t){return(_setPrototypeOf=Object.setPrototypeOf||function _setPrototypeOf(e,t){return e.__proto__=t,e})(e,t)}var d=function(e){function ConfirmationWall(){return function _classCallCheck(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,ConfirmationWall),_possibleConstructorReturn(this,_getPrototypeOf(ConfirmationWall).apply(this,arguments))}return function _inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&_setPrototypeOf(e,t)}(ConfirmationWall,n.a.Component),function _createClass(e,t,r){return t&&_defineProperties(e.prototype,t),r&&_defineProperties(e,r),e}(ConfirmationWall,[{key:"render",value:function render(){var e=this.props,t=e.isOpen,r=e.wallOverlayType,o=e.children,s=e.action,p=e.actionText,u=e.cancel,d=e.cancelText,m=c()({[f.a.dialogButton]:!0}),h=c()({[f.a.dialogButton]:!0});return n.a.createElement(a.a,{isOpen:t,responseRequired:!0,padding:!0,shouldFocusOnMount:!0,overlayType:r},n.a.createElement("div",null,o,n.a.createElement(l.a,{center:!0},n.a.createElement(i.a,{theme:"primary",outline:!0,className:m,onClick:s},p),n.a.createElement(i.a,{theme:"platform",outline:!0,className:h,onClick:u},d))))}}]),ConfirmationWall}();d.defaultProps={wallOverlayType:"transparent",actionText:p.confirm,cancelText:p.cancel},t.a=d},iPqP:function(e,t,r){e.exports={fileDropzone:"fileDropzone__1QiPO2UViwLqWFeGgKAddB",dragActive:"dragActive__HLAi3XyTvXqmiNyoaHpCR"}},rtHi:function(e){e.exports=JSON.parse('{"cancel":"Cancel","confirm":"Confirm"}')},volc:function(e,t,r){e.exports={fileTool:"fileTool__3fRqxfr_8Xp4mGcZjaaBdh",fileToolClosed:"fileToolClosed__GPJjW0eccgFKvJeJRAfKI",fileToolIsAdding:"fileToolIsAdding__1TBScRTF1ZxdsN1YElfQSV",fileToolError:"fileToolError__1wErKpCEe9II71CXjmV1L6",fileToolContainer:"fileToolContainer__2r2FHFLKxbL8s4jyUYPbww"}},zeeO:function(e,t,r){e.exports={folderItem:"folderItem__3u66r1wD0f0OYNCAkMN7Cv",fileTreeTreeBtn:"fileTreeTreeBtn__1x5DnY83QQkqbDHCmxsRXI",fileTreeTreeBtnActive:"fileTreeTreeBtnActive__10qUKyzaqpfs-kdGkfF3Gp",fileTreeTreeBtnInactive:"fileTreeTreeBtnInactive__rvaADe14tcciv7UzZIfO1",itemName:"itemName__26pDYv9w-_SR8yDMUVyC3_",renameForm:"renameForm__zpH099Iiwq8dgdvjsiI44",renameFormInput:"renameFormInput__18HVRsxdSVwmFGnsNw-RnR",rightIcons:"rightIcons__lYvxfR1zG-Qgb4GS3_IuH",dropdown:"dropdown__1ohW441HJYFkzcMu2dxHbe",dropdownOption:"dropdownOption__2CNQE_Jojqf1MQNNHwT1z2",icon:"icon__3MZ-1lVeElHHMs4AZWgFO6"}}}]);
//# sourceMappingURL=100.199bb2b67b2fd5d671c3.chunk.js.map