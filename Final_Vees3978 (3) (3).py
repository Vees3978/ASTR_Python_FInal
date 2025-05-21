<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Final_Vees3978</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: #ffffcc }
.highlight { background: #f8f8f8; }
.highlight .c { color: #3D7B7B; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #3D7B7B; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #3D7B7B; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #9C6500 } /* Comment.Preproc */
.highlight .cpf { color: #3D7B7B; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #3D7B7B; font-style: italic } /* Comment.Single */
.highlight .cs { color: #3D7B7B; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #E40000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #008400 } /* Generic.Inserted */
.highlight .go { color: #717171 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #687822 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #717171; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #CB3F38; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #767600 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #AA5D1F; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #A45A77; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #A45A77 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="2.-write-calculation-tools:">2. write calculation tools:<a class="anchor-link" href="#2.-write-calculation-tools:">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>2.1 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">forces</span> <span class="k">as</span> <span class="nn">F</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mEarth</span> <span class="o">=</span> <span class="mf">6.0e24</span>     <span class="c1"># kg</span>
<span class="n">mPerson</span> <span class="o">=</span> <span class="mf">70.0</span>      <span class="c1"># kg</span>
<span class="n">radiusEarth</span> <span class="o">=</span> <span class="mf">6.4e6</span> <span class="c1"># m</span>
<span class="nb">print</span><span class="p">(</span><span class="n">F</span><span class="o">.</span><span class="n">forceMagnitude</span><span class="p">(</span><span class="n">mEarth</span><span class="p">,</span><span class="n">mPerson</span><span class="p">,</span><span class="n">radiusEarth</span><span class="p">))</span>

<span class="c1"># I exprect this to be 693.935. I know this because there is examples in the py function</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>683.935546875
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">someplace</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">3.0</span><span class="p">,</span><span class="mf">2.0</span><span class="p">,</span><span class="mf">5.0</span><span class="p">])</span>
<span class="n">someplaceelse</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">1.0</span><span class="p">,</span> <span class="o">-</span><span class="mf">4.0</span><span class="p">,</span> <span class="mf">8.0</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="n">F</span><span class="o">.</span><span class="n">unitDirectionVector</span><span class="p">(</span><span class="n">someplace</span><span class="p">,</span> <span class="n">someplaceelse</span><span class="p">))</span> 
<span class="c1">#I was able to use the example in the force.py to see if this is correct</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[-0.28571429 -0.85714286  0.42857143]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mEarth</span> <span class="o">=</span> <span class="mf">6.0e24</span>     <span class="c1"># kg</span>
<span class="n">mPerson</span> <span class="o">=</span> <span class="mi">1</span>      <span class="c1"># kg</span>
<span class="n">radiusEarth</span> <span class="o">=</span> <span class="mf">6.4e6</span> <span class="c1"># m</span>
<span class="n">centerEarth</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">])</span>
<span class="n">surfaceEarth</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span><span class="o">*</span><span class="n">radiusEarth</span>
<span class="nb">print</span><span class="p">(</span><span class="n">F</span><span class="o">.</span><span class="n">forceVector</span><span class="p">(</span><span class="n">mEarth</span><span class="p">,</span> <span class="n">mPerson</span><span class="p">,</span> <span class="n">centerEarth</span><span class="p">,</span> <span class="n">surfaceEarth</span><span class="p">))</span>
<span class="c1">#I know that this is correct becaause I know what the force from the earth is</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[0.         0.         9.77050781]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>2.2 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">leapfrog</span> <span class="kn">import</span> <span class="n">updateParticles</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">help</span><span class="p">(</span><span class="n">updateParticles</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Help on function updateParticles in module leapfrog:

updateParticles(masses, positions, velocities, dt)
    Evolve particles in time via leap-frog integrator scheme. This function
    takes masses, positions, velocities, and a time step dt as
    
    Parameters
    ----------
    masses : np.ndarray
        1-D array containing masses for all particles, in kg
        It has length N, where N is the number of particles.
    positions : np.ndarray
        2-D array containing (x, y, z) positions for all particles.
        Shape is (N, 3) where N is the number of particles.
    velocities : np.ndarray
        2-D array containing (x, y, z) velocities for all particles.
        Shape is (N, 3) where N is the number of particles.
    dt : float
        Evolve system for time dt (in seconds).
    
    Returns
    -------
    Updated particle positions and particle velocities, each being a 2-D
    array with shape (N, 3), where N is the number of particles.

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mass</span><span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="c1">#(1)</span>
<span class="n">positions</span><span class="o">=</span> <span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])]</span> <span class="c1">#(1,1,1)</span>
<span class="n">velocities</span><span class="o">=</span> <span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">])]</span>
<span class="n">dt</span><span class="o">=</span><span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">updateParticles</span><span class="p">(</span><span class="n">mass</span><span class="p">,</span> <span class="n">positions</span><span class="p">,</span> <span class="n">velocities</span><span class="p">,</span> <span class="n">dt</span><span class="p">))</span>

<span class="c1">#this gives the updated particle positions and velocities. This should be in a 2d array</span>

<span class="c1">#the order of this is (position, velocity)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(array([[2., 2., 2.]]), array([[1., 1., 1.]]))
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>2.3 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">calculateTrajectories</span><span class="p">(</span><span class="n">masses</span><span class="p">,</span> <span class="n">positions_0</span> <span class="p">,</span> <span class="n">velocities_0</span><span class="p">,</span> <span class="n">dt</span><span class="p">,</span> <span class="n">t_max</span> <span class="o">=</span> <span class="mi">0</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39;</span>
<span class="sd">    Purpose</span>
<span class="sd">    -------</span>
<span class="sd">    the prpose of this funtion is to change the the particles initial </span>
<span class="sd">    positions and inital velocites over some time. </span>
<span class="sd">    </span>
<span class="sd">    How it works</span>
<span class="sd">    ------------</span>
<span class="sd">    This will use a loop so that it is updating the the position and velocities at at each point in time.</span>
<span class="sd">    Each time that it updates these positions and velocities it should be storing it in an array.</span>
<span class="sd">    </span>
<span class="sd">    Atributes</span>
<span class="sd">    ---------</span>
<span class="sd">    mass = 1D array of the N particle elements </span>
<span class="sd">    Position_0 = the intial position of the particles(2D array)</span>
<span class="sd">    Velocities_0 = this is the initial velocites of each particle (2D array)</span>
<span class="sd">    dt = this is the step size (in seconds)</span>
<span class="sd">    t = the total time need to evolve the system (in seconds) aka this is the max time </span>
<span class="sd">    </span>
<span class="sd">    return</span>
<span class="sd">    ------</span>
<span class="sd">    times = this should be in a 1D array of each time step (this includes t_0)</span>
<span class="sd">    positions = this should be a multi-dimensional array of all the positions at some time</span>
<span class="sd">    velocities= This thould also print multi-dimensional array of all the velocities at some time</span>
<span class="sd">    </span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">Pos</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">Vel</span> <span class="o">=</span><span class="p">[]</span>
    <span class="c1">#this will just be where all of the positions and velocities will go</span>
     <span class="c1">#this will be the array for time</span>
 <span class="c1">#I definded this so that it will start at 0 and add the step size each time</span>
    <span class="n">time</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">t_max</span><span class="o">+</span><span class="n">dt</span><span class="p">,</span><span class="n">dt</span><span class="p">)</span>

   <span class="c1">#print(masses)</span>
    <span class="c1">#print(positions_0)</span>
    <span class="c1">#print(velocities_0)</span>
    <span class="c1">#I am trying to add all of the times into an array up to what t_max at the step size of dt</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">time</span><span class="p">)):</span>
             <span class="c1">#I am trying to make it so that it takes the velocity and position at each time and adds it to a new array</span>
        <span class="n">P</span><span class="p">,</span> <span class="n">V</span> <span class="o">=</span> <span class="n">updateParticles</span><span class="p">(</span><span class="n">masses</span><span class="p">,</span> <span class="n">positions_0</span><span class="p">,</span> <span class="n">velocities_0</span><span class="p">,</span> <span class="n">dt</span><span class="p">)</span>
        <span class="n">Pos</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">P</span><span class="p">)</span>
        <span class="n">Vel</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">V</span><span class="p">)</span>
        <span class="n">positions_0</span> <span class="o">=</span> <span class="n">P</span>
        <span class="n">velocities_0</span> <span class="o">=</span> <span class="n">V</span>
        <span class="c1">#print(P)</span>
        <span class="c1">#I want this to print time, position, and velocity in differet colums so that it is easier to extract the data</span>
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">Pos</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">Vel</span><span class="p">]),</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">time</span><span class="p">])</span>    
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I am stuck on how to write this for loop so that it is updating the time at each step and putting it into an array with position and velocity
I know that the updateParticles function returns the end positions and velocity but I am not sure how to make it so that it will add to the previouse end possition and velocity to the array along with an updated times. 
I would be extreemly greatful for any advice for this section. I think that I might be over simplifying what should be done in this step and see a push in the right direction would be nice. I have been stuck on this section for a couple days now and have restarted many times! I am very confused!
I know we have done similar things in homework B but now it is using a previously defined function.
<em>Please help</em></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="3.-Earth-in-(circular)-orbit-around-the-sun.">3. Earth in (circular) orbit around the sun.<a class="anchor-link" href="#3.-Earth-in-(circular)-orbit-around-the-sun.">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>3.4 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">au</span><span class="o">=</span><span class="mf">1.49e11</span> <span class="c1">#This will help convert from au to meters</span>
<span class="n">MassS</span> <span class="o">=</span>  <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mf">1.989e30</span><span class="p">,</span> <span class="mf">5.972e24</span><span class="p">])</span> 
<span class="n">PosS</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="o">-</span><span class="mf">3e-6</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">],[</span><span class="mf">0.999997</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span><span class="o">+</span><span class="mf">0.0e+00</span><span class="p">]])</span><span class="o">*</span><span class="n">au</span>
<span class="n">VelS</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span><span class="o">-</span><span class="mf">8.94e-2</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">],[</span><span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span> <span class="mf">2.98e4</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">]])</span>
<span class="n">time</span> <span class="o">=</span> <span class="mi">1000</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span> <span class="c1">#I am convertining it to seconds</span>
<span class="n">stept</span> <span class="o">=</span> <span class="mf">0.1</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span> <span class="c1">#I am converting it to seconds</span>

<span class="n">Pos</span><span class="p">,</span> <span class="n">Vel</span><span class="p">,</span> <span class="n">Time</span> <span class="o">=</span><span class="n">calculateTrajectories</span><span class="p">(</span><span class="n">MassS</span><span class="p">,</span> <span class="n">PosS</span> <span class="p">,</span> <span class="n">VelS</span><span class="p">,</span> <span class="n">stept</span><span class="p">,</span> <span class="n">time</span> <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>For this section once I finally figure out how to properly define the function, I should be able to create a 1D array with the mass of the earth and the sun.
Then I will have to create two 2D arrays for the position and velocity of the earth and the sun.
Then after this I can plug them into the function calculateTrajectories. 
the step size will be converted to 0.1 days to seconds, and 1000 days will be converted to seconds as well as that is what our functions units are. 
This should give us the array of (position, velocity, and time.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>3.5 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Pos</span><span class="o">.</span><span class="n">ndim</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Pos</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Time</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">Pos_all</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Pos</span><span class="p">)</span><span class="o">/</span><span class="n">au</span> <span class="c1">#I divid by au so that these plot for position will be back in units of au</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Pos_all</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">Time_SE</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Time</span><span class="p">)</span><span class="o">/</span><span class="mi">24</span><span class="o">/</span><span class="mi">60</span><span class="o">/</span><span class="mi">60</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Time_SE</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1">#I was jsut trying to fix the shape of the arrays. It wouldn&#39;t let me plot becuase of the shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>4
(1, 10001, 2, 3)
(1, 10001)
(10001, 2, 3)
(10001,)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE</span><span class="p">,</span> <span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">)</span> <span class="c1">#This is using the first mass, 1st row, and the x value of the position</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE</span><span class="p">,</span> <span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Earth&#39;</span><span class="p">)</span><span class="c1">#I follow a similar thing to the line above</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span> <span class="c1">#This is just so I know which color is which </span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth Position Vs. Time&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Position(m)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Time(Days)&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It seems like the period is just over 3e7 so this should be just over 340 days. Which makes sense since there are 365 days in a year.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span><span class="c1">#This helps to make the image larger.</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">Pos_all</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Earth&#39;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth xy-trajectories&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(y)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(x)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">(</span><span class="s1">&#39;scaled&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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okUsW7aMTp06rTdPUpGZFZRdx7vCq+Xatw+H9999F/7w582LOyKXL1atWkWrVq1YulR8/HH4R9ylS+1NoACSaNWq1Xq176p4Eq0j1qyBJ54IneKeeWbc0bh88eWXYubM0BPTZnXklhZV87+EJ9E65NhjYfXq0CGEBD/+GHdELld9+CF8+21o5bH77uH8Z1yuvfZaunXrRvfu3enRowcffPBBfMGUwy8s1TElfZLeey+0agUnnQT//nfcUblcsW4d7LMPfPwxfPIJtG1b9TqZ9L///Y8xY8bw8ccfs9FGG7Fw4UJWr14db1BleBKto846Kww50rAhPPIITJ0KXbvGHZWL0+jRYTyve+6BDz5IuPL+nyycBD2h/Avc8+bNo3Xr1my00UYAtG7dGoCOHTtSWFhI69atKSws5KKLLuLNN99k6NChzJo1i6+++opZs2Zx/vnnc95552U0dD+cr8MaNAi10ldfhW7dwiF+cXHcUbls+/770Jb4wgvh55/DP9hccfDBBzN79mx22GEHzj77bN56660q1/n8888ZP348H374IVdffTVr1qzJaIyeRB0HHhiS6cEHh3NfF10Ud0QuG4qLQ2P5tm3hjTdg5kxo2jTuqNbXrFkzioqKGD58OG3atOHYY4/loYceqnSdQw89lI022ojWrVuz+eabM3/+/EqXT5UnUfer8eNDTeSWW0Kt9L//jTsilyl33BH+Yf72t+EfaK9ecUdUsfr169OnTx+uvvpq7rrrLp555hkaNGhAcXTYVLY5Usmhf8m6a9euzWh8nkTdepo2DT+qzz4LtRSpdt6VUlc991z4Tl96KTR7u6SyrtBzwBdffMH06dN/fT9x4kS22WYbOnbsSFFREQDPPPNMXOEBfmHJVWCnnUIyff750gtOX38NHTvGGparobffDuMdde8OS5dC8+bVWLmCiz7ZsHz5cs4991wWL15MgwYN2H777Rk+fDjTpk3j9NNP57rrrmPPPfeMLT7w2z5dkh54AM44I7yeORO23TbeeFxyXnklnOtu3z60/dxyy+TXnTZtGjvttFPmgsth5e273/bpUnL66aFm+sADYYA8Cd5/P+6oXEWeeip8R0OGwPz5MGtW9RKoS54nUVctp50Wkum4cbD33uGHetddcUflIFxtv+SS8J3cdlvobemLL0Kfny5zPIm6GjnkkJBMv/oKzj03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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Vel_SE</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Vel</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Vel_SE</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span> <span class="c1">#I just wanted to check to make sure this will work </span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(10001, 2, 3)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE</span> <span class="p">,</span><span class="n">Vel_SE</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth xy-trajectories&#39;</span><span class="p">)</span> <span class="c1">#I just wanted to make sure to label it so I will know what each graph represents</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Velocity(m/s))&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Time(Days)&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Based on this graph it seems like the perciction of radial velocity that we would need to see an earth like planet orbiting a sun like star would need between 0.09 m/s to 0.1 m/s. So this seems like it would probably be hard.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>!!This was my Seudo-code!!</p>
<p>The first plot will be a time vs. postition axis. This will use all of the arrays on the time row and all of the arrays in the position row. we can call these by using [:,0,0] and [:,1,0]. I believe this should be able to pull out those individual sections</p>
<p>then I will make an xy-axis plot. this should follow very similar things to the previouse plot.</p>
<p>Lastly, I am not sure what this is asking. Should the function give an x and y for both velocity and position?</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>3.6 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">VelTwo</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span><span class="o">-</span><span class="mf">8.94e-2</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">],[</span><span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">,</span> <span class="mf">2.98e4</span><span class="p">,</span> <span class="o">+</span><span class="mf">0.0000e+00</span><span class="p">]])</span><span class="o">/</span><span class="mi">2</span><span class="c1">#This is decresinf it by a factor of two</span>
<span class="n">Pos2</span><span class="p">,</span> <span class="n">Vel2</span><span class="p">,</span> <span class="n">Time2</span> <span class="o">=</span><span class="n">calculateTrajectories</span><span class="p">(</span><span class="n">MassS</span><span class="p">,</span> <span class="n">PosS</span> <span class="p">,</span> <span class="n">VelTwo</span><span class="p">,</span> <span class="n">stept</span><span class="p">,</span> <span class="n">time</span> <span class="p">)</span>

<span class="n">Pos_SE2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Pos2</span><span class="p">)</span><span class="o">/</span><span class="n">au</span> <span class="c1">#I divid by au so that these plot for position will be back in units of au</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Pos_SE2</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="n">Time_SE2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Time2</span><span class="p">)</span><span class="o">/</span><span class="mi">24</span><span class="o">/</span><span class="mi">60</span><span class="o">/</span><span class="mi">60</span>
<span class="n">Vel_SE2</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Vel2</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE2</span><span class="p">,</span> <span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE2</span><span class="p">,</span> <span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Earth&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth Position Vs. Time (V decreased by a factor of 2)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Position(m)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Time(Days)&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>(10001, 2, 3)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">Pos_all</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">Pos_SE2</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Earth&#39;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth xy-trajectories (V decreased by a factor of 2)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(y)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(x)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">(</span><span class="s1">&#39;scaled&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The orbit seems a lot different than before. This seems more like an eliptical than a perfect circle now. Which I think is very intresting. This is if the graph is scaled. If it is not scaled then it seems like the graph is a perfect cirtcle. But if I make this graph exactly like how I did in 3.5 then it looks like what it is above. The graph makes a lot more sense now because when the object is closer to the sun it will move faster than when it is further from it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE2</span> <span class="p">,</span><span class="n">Vel_SE2</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Sun&#39;</span><span class="p">)</span> <span class="c1">#This is the just to plot the graph </span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">Time_SE2</span> <span class="p">,</span><span class="n">Vel_SE2</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Earth&#39;</span><span class="p">)</span><span class="c1">#this is just the y of the points.</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Sun and Earth xy-trajectories (V decreased by a factor of 2)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Velocity(m/s))&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Time(Days)&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The velocity graph seems to be the most different. It no longer seems like it is perfectly ocilating but this does make sense since the orbit is no longer a perfectly circular orbit.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="4.--The-circumbinary-Exoplanet-Kepler-16-ABb:">4.  The circumbinary Exoplanet Kepler-16 ABb:<a class="anchor-link" href="#4.--The-circumbinary-Exoplanet-Kepler-16-ABb:">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>4.7 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>

<span class="c1">###I commented it out beceause I wasn&#39;t sure how to get all the positions correct but I do try it again and I think I was succesful later</span>

<span class="c1">#loads the file into this notebook</span>
<span class="c1">#files =&#39;/home/vees3978/Final_Project_2600/&#39; #I should make sure to pay attention to what folder I downloaded it to</span>

<span class="c1">#this takes the files from each file</span>
<span class="c1">#kepler16 = pd.read_csv(&#39;kepler16.txt&#39;,sep=&#39; &#39;, skiprows=1, names=[&quot;mass (kg)&quot;, &quot;x(m)&quot;,&quot;y(m)&quot;,&quot;z (m)&quot;,&quot;vx (m/s)&quot;, &quot;vy (m/s)&quot;,&quot;vz (m/s)&quot;])</span>

<span class="c1">#Mass3= kepler16[&quot;mass (kg)&quot;].values </span>
<span class="c1">#x= kepler16[&quot;x(m)&quot;].values</span>
<span class="c1">#y=kepler16[&quot;y(m)&quot;].values</span>
<span class="c1">#z=kepler16[&quot;z (m)&quot;].values</span>
<span class="c1">#vx=kepler16[&quot;vx (m/s)&quot;].values</span>
<span class="c1">#vy=kepler16[&quot;vy (m/s)&quot;].values</span>
<span class="c1">#vz=kepler16[&quot;vz (m/s)&quot;].values</span>

<span class="n">MassKep</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="o">+</span><span class="mf">1.3718e+30</span><span class="p">,</span><span class="o">+</span><span class="mf">4.0287e+29</span><span class="p">,</span> <span class="o">+</span><span class="mf">6.3250e+26</span><span class="p">])</span>
<span class="n">KepP</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="o">+</span><span class="mf">7.6349e+09</span><span class="p">,</span><span class="o">-</span><span class="mf">9.6587e+05</span><span class="p">,</span> <span class="o">+</span><span class="mf">1.8447e+09</span><span class="p">],[</span><span class="o">-</span><span class="mf">2.5998e+10</span><span class="p">,</span><span class="o">+</span><span class="mf">3.2889e+06</span><span class="p">,</span><span class="o">-</span><span class="mf">6.2813e+09</span><span class="p">],[</span><span class="o">+</span><span class="mf">3.7761e+10</span><span class="p">,</span><span class="o">-</span><span class="mf">4.0923e+07</span><span class="p">,</span><span class="o">+</span><span class="mf">8.1934e+10</span><span class="p">]])</span>
<span class="n">KepV</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([[</span><span class="o">-</span><span class="mf">1.0502e+03</span><span class="p">,</span><span class="o">-</span><span class="mf">6.8224e+00</span><span class="p">,</span><span class="o">+</span><span class="mf">1.3030e+04</span><span class="p">],[</span><span class="o">+</span><span class="mf">3.5760e+03</span><span class="p">,</span><span class="o">+</span><span class="mf">2.3231e+01</span><span class="p">,</span><span class="o">-</span><span class="mf">4.4368e+04</span><span class="p">],[</span><span class="o">-</span><span class="mf">3.6298e+04</span><span class="p">,</span><span class="o">-</span><span class="mf">1.0812e+01</span><span class="p">,</span><span class="o">+</span><span class="mf">1.7020e+04</span><span class="p">]])</span>


<span class="c1">#KepPos,KepVel,KepTime=calculateTrajectories(MassKep,KepP, KepV , KepDt, TimeK)</span>

<span class="c1">#TimeKep = np.squeeze(KepTime)</span>
<span class="c1">#VelKep = np.squeeze(KepVel)</span>
<span class="c1">#PosKep = np.squeeze(KepPos)</span>

<span class="c1">#print(KepP[0,0])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>4.8 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">KepPor</span><span class="o">=</span><span class="p">[]</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">MassKep</span><span class="p">)):</span>
    <span class="n">KepPor</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MassKep</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">/</span><span class="n">np</span><span class="o">.</span><span class="n">max</span><span class="p">(</span><span class="n">MassKep</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span><span class="c1">#This helps to make the image larger.</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;orange&#39;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s1">&#39;Star 1&#39;</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="n">KepPor</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span><span class="c1">#this is the first object</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">&#39;Blue&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Star 1&#39;</span><span class="p">,</span><span class="n">s</span><span class="o">=</span><span class="n">KepPor</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span><span class="c1">#this is the second object</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;Red&#39;</span><span class="p">,</span><span class="n">label</span><span class="o">=</span><span class="s1">&#39;Planet&#39;</span><span class="p">,</span><span class="n">linewidth</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span><span class="n">s</span><span class="o">=</span><span class="n">KepPor</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span><span class="c1">#this is the third object</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Kepler xz-trajectories&#39;</span><span class="p">)</span><span class="c1">#I just wanted to tittle it so that it is clear</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span><span class="c1">#This so I know what each color means</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(x)&#39;</span><span class="p">)</span><span class="c1">#This is just the label</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;Trajectory(z)&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">quiver</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span><span class="c1">#I had to do each vector for each point in different rows so that it would work well  </span>
<span class="n">plt</span><span class="o">.</span><span class="n">quiver</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">plt</span><span class="o">.</span><span class="n">quiver</span><span class="p">(</span><span class="n">KepP</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepP</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">0</span><span class="p">],</span> <span class="n">KepV</span><span class="p">[</span><span class="mi">2</span><span class="p">,</span><span class="mi">2</span><span class="p">]);</span>
<span class="c1">#The planet is really small but I hope that the legend helps to know its there with the velocity vector.</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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ayklSXuRnBTrGh3xP76VXIfvAUbESuDl+t2udHfk4FY+9gBwnKQd05Mfx6XTLN+GAIsdflavwwWgpFuBx4H9JC2RdBZwGnCWpGdIdoPqj48cImkJyTVb19efMYyIt4EfALPT1+XpNMspSReSHEv+drlrsY6jQ+4Cm5mVQofrAZqZlYoD0Mxyq0ONTNGnT5+oqakpdxlm1snMmTPnrYjo23h6hwrAmpoaamtry12GmXUykl5parp3gc0stxyAZpZbDkAzy60OdQywKevWrWPJkiV88MEH5S6lrLp3707//v2prvZISFb5Nm7cyCuvvMKAAQOoqirfkww6fAAuWbKEXr16UVNTQ8PRm/IjIlixYgVLlixh4MCB5S7HbIt16dKFmTNnMnToUAYMGMC+++7b4LXPPvuw6667Zv473+ED8IMPPsh1+AFIYuedd6aurq7cpZhtNaeddhq77LILn//851m4cOFm83v27Ml+++3HddddxyGHHJJJDRVxDDDP4VfP28A6o2OPPZZHH32Uj31s8+c8rVmzhksvvTSz8IMKCcCirVoET54Dt/WGW7okX588J5m+BX74wx8yePBgDjroIIYNG8asWbMAuPrqq3n//fe3aNmPPfYYI0aMoGvXrkyfPn2LlmVWiUaMGMHMmTPZZ599GkzfsGEDl1xyCb/61a/48MMPM1l35wnApffBvQfBoimwfhUQyddFU5LpS+9r12Iff/xx7rnnHp566inmzZvHH//4R/bYYw+gfQG4YUPDwXwHDBjA1KlT+eIXmxy42CwX9tprL2bOnMmhhybjwHbp0oUddtiBF154gYkTJzJw4ECuuOIKVq5cuVXX2zkCcNUi+PPJsOF9iHUN58W6ZPqfT25XT3DZsmX06dOHbbbZBoA+ffrQr18/rr32WpYuXcqYMWMYM2YMAN/4xjcYNWoUgwcP5rLLLtu0jJqaGi6//HI++clPcvvttzdYfk1NDQcddBBdunSOfwqz9urTpw8PP/wwJ554Ittssw2vvvoqV155Jf369WPZsmVccsklDBgwgBde2Ozx0+3WOX7rFl4FG9e13GbjOnjup21e9HHHHcdrr73GvvvuyznnnMOjjz4KwHnnnUe/fv2YMWMGM2bMAJJd5draWubNm8ejjz7KvHnzNi2ne/fu/OUvf2H8+PFtrsEsL3r06MEdd9zBGWecQa9evbjooot46aWXmDJlCvvuuy8DBgxg78cf32rr6xwBuPjmzXt+jcU6WHxTmxfds2dP5syZw+TJk+nbty+nnHIKU6dObbLtbbfdxogRIxg+fDjz589nwYIFm+adcsopbV63WR517dqVSZM+ejTMNttsw1lnncWCBQu499570Ze23kPxMr0MRtK/AmeTPJDor8CXI2LrX9G8fnVx7dYV2a6RqqoqjjzySI488kiGDh3Kb3/7WyZMmNCgzcsvv8yVV17J7Nmz2XHHHZkwYUKDi7d79OjRrnWb5VFTVz1UVVXRv3//rbqezHqAknYneeThqIgYAlQB2ez/de1ZXLvqItsVeP755xscc5g7dy577pk8HbFXr16sWrUKgJUrV9KjRw+233573njjDe67r30nXcysdLK+ELorsK2kdcB2NP3g7S1Xc3pytrel3WBVQ80ZbV706tWrOffcc3n33Xfp2rUre++9N5MnTwZg4sSJjB07lt12240ZM2YwfPhwBg8ezF577cVhhx1W1PJnz57N5z73Od555x3uvvtuLrvsMubPn9/mOs2s7TJ9Joik80merboGeDAiTmup/ahRo6LxeIALFy7kgAMOaHlFqxYll7psaOGSlKrt4IR50GtQccV3QEVtCzPbjKQ5ETGq8fQsd4F3JHl620CgH9BD0ulNtJsoqVZSbbtv9eo1CA6fnoScGg0WoOpk+uHTKzr8zGzry/Is8DHAyxFRFxHrgN8D/9C4UURMjohRETGqb9/NRqwuXr+xSQ9v74lQ3Rvoknzde2Iyvd/Y9i/bzDqlLI8Bvgp8XNJ2JLvARwPZjnffaxAc8vPkZWbWisx6gBExC5gOPEVyCUwXkgdTm5l1CJmeBY6Iy4DLWm1oZlYGneNOEDOzdnAAFsHDYZl1Tg7AVng4LLPOq9MF4PLlcPHF8KlPJV+XL9+y5Xk4LLPOq1P91i1fDkOHwrXXwmOPJV+HDt2yEPRwWGadV6cKwKuugpUrYe3a5P3atcn7q65q/zI9HJZZ59XhnwrXFk8++VH41Vu7Npm+JTwcllnn1Kl6gKNHQ7duDad16wbpYwbaxcNhmXVenaoHeNFFMHXqR7vB3bpB795w4YXtX6aHwzLrvDIdDqut2j0cVoHly5Njfk8+mfQIL7oIdt11a1daHh4Oy6x9mhsOq1P1ACEJuyuuKHcVZlYJOtUxQDOztnAAmlluOQDNLLccgGaWWw5AM8stB2ARqqqqGDZsGEOGDGHcuHGbRoDp2bPtzxluzR133NHgFjozy44DsAjbbrstc+fO5dlnn6Vbt25MmjQps3U5AM1KxwHYRocffjgvvvhig2mrV6/m6KOPZsSIEQwdOpQ777wTgMWLF3PAAQfw1a9+lcGDB3PcccexZs0aABYtWsTxxx/PyJEjOfzww3nuueeYOXMmd911FxdffDHDhg1j0aJFJf/5zHIlIjrMa+TIkdHYggULNptWaj169IiIiHXr1sVJJ50Uv/zlLzeb/t5770VERF1dXQwaNCg2btwYL7/8clRVVcXTTz8dERHjxo2Lm266KSIijjrqqPjb3/4WERFPPPFEjBkzJiIizjzzzLj99tubrKMjbAuzSgTURhOZ0+nuBMnCmjVrGDZsGJD0AM8666wG8yOC7373uzz22GN06dKF119/nTfeeAOAgQMHbvrsyJEjWbx4MatXr2bmzJmMGzdu0zI+/PDDkvwsZvaRzhuAN90EZ5yxVRZVfwywOdOmTaOuro45c+ZQXV1NTU3NpqGw6keShuRkypo1a9i4cSM77LBDi8s0s+x13mOAWyn8ivHee++xyy67UF1dzYwZM3jllVdabN+7d28GDhy4aXj8iOCZZ54BGg6xZWbZ6rwBWEKnnXYatbW1jBo1imnTprH//vu3+plp06Zxww03cPDBBzN48OBNJ07Gjx/PFVdcwfDhw30SxCxjnW44rM7M28KsfZobDss9QDPLLQegmeWWA9DMcqsiArAjHacsF28Ds62vwwdg9+7dWbFiRa4DICJYsWIF3bt3L3cpZp1Kh78Qun///ixZsoS6urpyl1JW3bt3p3///uUuw6xT6fABWF1dzcCBA8tdhpl1Qh1+F9jMLCsOQDPLLQegmeWWA9DMcssBaGa55QA0s9xyAJpZbjkAzSy3HIBmllsOQDPLLQegmeWWA9DMcssBaGa55QA0s9xyAJpZbmUagJJ2kDRd0nOSFkr6RJbrMzNri6wHRL0GuD8iTpbUDdgu4/WZmRUtswCU1Bs4ApgAEBFrgbVZrc/MrK2y3AXeC6gDfiPpaUlTJPXIcH1mZm2SZQB2BUYA10XEcODvwLcbN5I0UVKtpNq8P/jIzEorywBcAiyJiFnp++kkgdhAREyOiFERMapv374ZlmNm1lBmARgRy4HXJO2XTjoaWJDV+szM2irrs8DnAtPSM8AvAV/OeH1mZkXLNAAjYi4wKst1mJm1l+8EMbPccgCaWW45AM0stxyAZpZbDkAzyy0HoJnllgPQzHLLAWhmueUANLPccgCaWW45AM0stxyAZpZbDkAzyy0HoJnllgPQzHLLAWhmueUANLPccgCaWW45AM0stxyAZpZbDkAzyy0HoJnllgPQzHLLAWhmueUANLPccgCaWW45AM0st7q2NFPSJ4DTgcOB3YA1wLPA/wA3R8R7mVdoZpaRZnuAku4DzgYeAI4nCcADgUuB7sCdkk4qRZFmZlloqQd4RkS81WjaauCp9HWVpD6ZVWZmlrFme4D14SfpwMbzJB1Z2MbMrBIVcxLkNknfUmJbST8DfpR1YWZmWSsmAA8F9gBmArOBpcBhWRZlZlYKxQTgOpKzv9uSnPx4OSI2ZlqVmVkJFBOAs0kC8BDgk8CpkqZnWpWZWQm0eB1g6qyIqE2/Xw58VtIZGdZkZlYSLV0H2BOgIPw2iYibCtuYmVWilnaB75R0laQjJPWonyhpL0lfkVR/gbSZWUVqdhc4Io6WdALwNeAwSTsC64HnSW6FOzMilpemTDOzra/FY4ARcS9wb4lqMTMrqVbPAkuaLukESR45xsw6lWJCbRJwGvCCpP+UtH/GNZmZlUSrARgRf4yI04ARwGLgIUkzJX1ZUnXWBZqZZaWo3VpJOwMTSIbHehq4hiQQH8qsMjOzjLV6IbSk3wP7AzcBn4mIZems/ytps2sEzcwqRWsjQncB5kbE55uaHxGjMqnKzKwEWtwFTgc9GFuiWszMSqqYY4APSvqCJLVnBZKqJD0t6Z72fN7MLCvFDIZwIdAD2CBpDSAgIqJ3kes4H1gIFNvezKwkirkMpldEdImI6ojonb4vKswk9QdOBKZsaaFmZltbMT1A0qe/HZG+fSQiit2dvRq4BOjV9tLMzLJVzK1w/0myG7sgfZ2fTmvtc58G3oyIOa20myipVlJtXV1dkWWbmW05RUTLDaR5wLD6YfAlVQFPR8RBrXzuR8AZJCPIdCc5Bvj7iDi9uc+MGjUqamt9aaGZbV2S5jR12V6xAxzsUPD99sV8ICK+ExH9I6IGGA/8qaXwMzMrtWKOAf4IeFrSDJIzwEcA3820KjOzEmg1ACPiVkmPkDwUScC32joQakQ8AjzSjvrMzDJTzEmQhyNiWUTcFRF3RsRySQ+Xojgzsyw12wOU1B3YDuiTDodffydIb6BfCWozM8tUS7vAXwMuIAm7OXwUgCuBX2RblplZ9lp6KNI1wDWSzo2In5WwJjOzkijmMpiNknaofyNpR0nnZFeSmVlpFBOAX42Id+vfRMQ7wFczq8jMrESKCcAuhUNhpXeCdMuuJDOz0ijmQugHgNskTQIC+Dpwf6ZVmZmVQDEB+C2SM8LfIDkT/CAe3srMOoFi7gTZKGkqyb28z2dfkplZaRRzJ8hJwFzS3V5JwyTdlXFdZmaZK+YkyGXAaOBdgIiYC9RkVpGZWYkUE4DrI+K9zCsxMyuxYk6CPCvpi0CVpH2A84CZ2ZZlZpa9YnqA5wKDgQ+BW0nuBb4gw5rMzEqimLPA7wPfS19mZp1GS8NhXR0RF0i6m+QC6EIBvA1cHxFPZFmgmVlWWuoB3pR+vbKZ+X2AXwMHbtWKzMxKpKXhsOakXx9tro2ktVkUZWZWCq0eA0zP/P6IpKfXvX56ROwVEXdnWJuZWaaKOQv8G+A6kuf7jgFu5KPdYzOzilVMAG4bEQ+TPET9lYj4d+CobMsyM8teMRdCfyCpC/CCpH8BXgd2ybYsM7PsFdMDvIDk6XDnASOB04EzM6zJzKwkWuwBpqM//6+IuBhYDXy5JFWZmZVAsz1ASV0jYgMwsnBIfDOzzqKlHuCTwAjgaeBOSbcDf6+fGRG/z7g2M7NMFXMSZCdgBcmZ3yAZFj8AB6CZVbSWAnAXSRcCz/JR8NVrfG+wmVnFaSkAq4CeNAy+eg5AM6t4LQXgsoi4vGSVmJmVWEvXAfrMr5l1ai0F4NElq8LMrAyaDcCIeLuUhZiZlVoxt8KZmXVKDkAzyy0HoJnllgPQzHLLAWhmueUANLPccgCaWW45AM0stxyAZpZbDkAzyy0HoJnllgPQzHLLAWhmuZVZAEraQ9IMSQslzZd0flbrMjNrj2IeitRe64GLIuIpSb2AOZIeiogFGa7TzKxomfUAI2JZRDyVfr8KWAjsntX6zMzaqiTHACXVAMOBWaVYn5lZMTIPQEk9gd8BF0TEyibmT5RUK6m2rq4u63LMzDbJNAAlVZOE37SIaPJB6hExOSJGRcSovn37ZlmOmVkDWZ4FFnADsDAifpLVeszM2ivLHuBhwBnAUZLmpq8TMlyfmVmbZHYZTET8BT9b2Mw6MN8JYma55QA0s9xyAJpZbjkAzSy3HIBmllsOQDPLLQegmeWWA9DMcssBaGa55QA0s9xyAJpZbjkAzSy3HIBmllsOQDPLLQegmeWWA9DMcssBaGa55QA0s9xyAJpZbjkAzSy3HIBmllsOQDPLLQegmeWWA9DMcssBaGa55QA0s9xyAJpZbjkAzSy3HIBmllsOQDPLLQegdRrz589n/fr15S7DKogD0DqNu+++m/vvv7/cZVgFcQBapzFr1iymTJlS7jKsgnQtdwFmW0NEMGvWLN58802WLVvGbrvtVu6SrAK4B2idwpIlS1i2bBkbNmzgxhtvLHc5ViEcgNYpzJo1a9P3U6ZMISLKWI1VCgegdQqFAfjiiy/y2GOPlbEaqxQOQOsUCgMQ8MkQK4oD0Cre+vXrmTNnToNp06dP55133ilTRVYpHIBW8ebPn8/777/PTjvtBMCgQYPo06cPt9xyS5krs47OAWgVb+nSpfzud7/j+9//PgBDhw7l5ZdfZsyYMWWuzDo6B6BVvLFjx/L5Yw+m73t3AfDWwjvo+vudOHD1z2HVojJXZx2ZA9Aq39L74N6D6LvmTwDUrQTWr4JFU+Deg5L5Zk1wAFplW7UI/nwybHifPj03APDWqnRerIMN7yfz3RO0JjgArbItvAo2rgOgb69k0tt/hw0bC9psXAfP/bT0tVmH5wC0yrb45qSnB/TpBccMgfEfhw/WFrSJdbD4pvLUZx2aB0OwyrZ+9aZvq7vCQ99ppt261c3MsDzLtAco6XhJz0t6UdK3s1yX5VTXnsW1qy6yneVKZgEoqQr4BTAWOBA4VdKBWa3PcqrmdFB1y21UDTVnlKYeqyhZ9gBHAy9GxEsRsRb4b+CzGa7P8uiAi6BLKwHYpRr2/9fS1GMVJcsA3B14reD9knSa2dbTaxAcPh2qttu8J6jqZPrh05N2Zo1kGYBqYtpmg7RJmiipVlJtXV1dhuVYp9VvLJwwD/aeCNW9gS7J170nJtP7jS13hdZBZXkWeAmwR8H7/sDSxo0iYjIwGWDUqFEexdLap9cgOOTnycusSFn2AGcD+0gaKKkbMB64K8P1mZm1SWY9wIhYL+lfgAeAKuDXETE/q/WZmbVVphdCR8S9wL1ZrsPMrL18K5yZ5ZYD0MxyywFoZrnlADSz3HIAmlluOQDNLLccgGaWWw5AM8stB6CZ5VZFBuDy5XDxxfCpTyVfly8vd0VmVokq7pkgy5fD0KGwciWsXQtPPAFTp8Jf/wq77lru6sysklRcD/Cqqz4KP0i+rlyZTDcza4uKC8Ann6wPvxuAc4HZrF2bTDcza4uKC8DRo6FbN4DfAT8HnqFbNzj00PLWZWaVp+IC8KKLoHdv6NKlLwBVVXX07g0XXljmwsys4lRcAO66a3LCY/jwPgAMG/aWT4CYWbtUXABCEnYnn5z0AA88sM7hZ2btUnEBuGLFCjZs2EDfvkkA1tXVUVdXx4033ljmysys0lRcAC5fvpyBAwdyxx13AFBbW8t+++3HCy+8UN7CzKziVNyF0IMHD2b33XfnnnvuAeCtt94CYPTo0eUsy8wqUMX1AAHOPvvszaYd6utgzKyNKjIATznlFHr27LnpfU1NDbvssksZKzKzSlSRAdizZ0/Gjx+/6b17f2bWHhUZgNBwN9gBaGbtUbEBOHr0aIYMGQI4AM2sfRQR5a5hE0l1wCvlrqNAH+CtchfRAtfXfh25NnB9W6pxfXtGRN/GjTpUAHY0kmojYlS562iO62u/jlwbuL4tVWx9FbsLbGa2pRyAZpZbDsCWTS53Aa1wfe3XkWsD17eliqrPxwDNLLfcAzSz3HIAtkLSFZKekzRP0h8k7VDumgpJGidpvqSNkjrEWTlJx0t6XtKLkr5d7noKSfq1pDclPVvuWpoiaQ9JMyQtTP9dzy93TYUkdZf0pKRn0vq+X+6aGpNUJelpSfe01tYB2LqHgCERcRDwN+A7Za6nsWeBzwOPlbsQSP7zAb8AxgIHAqdKOrC8VTUwFTi+3EW0YD1wUUQcAHwc+OcOtv0+BI6KiIOBYcDxkj5e3pI2cz6wsJiGDsBWRMSDEbE+ffsE0L+c9TQWEQsj4vly11FgNPBiRLwUEWuB/wY+W+aaNomIx4C3y11HcyJiWUQ8lX6/iuQXeffyVvWRSKxO31anrw5zIkFSf+BEYEox7R2AbfMV4L5yF9HB7Q68VvB+CR3oF7iSSKoBhgOzylxKA+ku5lzgTeChiOhI9V0NXAJsLKZxxQ2ImgVJfwSaerLI9yLizrTN90h2T6aVsrZ03a3W14GoiWkdpodQKST1JHn26wURsbLc9RSKiA3AsPR4+B8kDYmIsh9TlfRp4M2ImCPpyGI+4wAEIuKYluZLOhP4NHB0lOG6odbq62CWAHsUvO8PLC1TLRVJUjVJ+E2LiN+Xu57mRMS7kh4hOaZa9gAEDgNOknQC0B3oLenmiDi9uQ94F7gVko4HvgWcFBHvl7ueCjAb2EfSQEndgPHAXWWuqWJIEnADsDAiflLuehqT1Lf+SghJ2wLHAM+VtahURHwnIvpHRA3J/7s/tRR+4AAsxs+BXsBDkuZKmlTuggpJ+pykJcAngP+R9EA560lPGP0L8ADJAfzbImJ+OWsqJOlW4HFgP0lLJJ1V7poaOQw4Azgq/f82N+3RdBS7ATMkzSP5Y/dQRLR6uUlH5TtBzCy33AM0s9xyAJpZbjkAzSy3HIBmllsOQDMrq7YMUCHpCElPSVov6eRG886U9EL6OrOYdTsArd0k7VxwqcZySa8XvO/WymdHSbq2neu9QNJ27au6yeVJ0p8k9W6hzR8l7bi11mkNTKX4ASpeBSYAtxROlLQTcBlwKMn96JcV8+/lALR2i4gVETEsIoYBk4Cf1r+PiLWSmr3TKCJqI+K8dq76AqBNAZiOUtOcE4BnWrnl7CbgnLas04rT1AAVkgZJul/SHEl/lrR/2nZxRMxj83t9/5HkmsS3I+IdklGcWg1VB6BtVZKmSvqJpBnAjyWNljQzHZ9tpqT90nZH1o/XJqlHuhs0O2332XR6laQrJf1VyXiM50o6D+hHcjHujLTdqWmbZyX9uKCW1ZIulzQLuFTSHwrmHSup/jaz04D6e76/XtCLfbl+HSR3s5ya5bazBiYD50bESOCbwC9bad+uQTh8L7BlYV/gmIjYkO5WHhER6yUdA/wf4AuN2n+P5Lalr6S3WT2ZDgDxJWAgMDz9/E4R8bakC4ExEfGWpH7Aj4GRwDvAg5L+KSLuAHoAz0bEv6W3mC2U1Dci6oAvA79J138Y8DWAiJgETErvx/0T8JN0+juStpG0c0SsyGCbWSodCOIfgNuTfzYAtmntY01Ma/UuDwegZeH2dMQQgO2B30rah+Q/ZHUT7Y8juYn9m+n77sAAkvtMJ9WPxxgRTY3jdwjwSBpqSJoGHAHcAWwgGVSAiAhJNwGnS/oNya2DX0qXsVM69l6ha0hC+e6CaW+S9D4dgNnqArybHlop1hLgyIL3/YFHilmR2db294LvfwDMiIghwGdIwq0xAV8oOH44ICIWptNb+yve1F/+eh8UBDEkPb7TSXZlby8Y6Ha9pE2/C5ImAHsCjYd77w6saaUe20LpsdiXJY2DTSepDm7lYw8Ax0naMT35cVw6rUUOQMva9sDr6fcTmmnzAHBuupuKpOHp9AeBr9efTEnP9AGsIhmgApLBQj8lqU96ouNU4NGmVhIRS0mG5rqU5MxjveeBvdJ11B9zOj0iNh1oT2vbFVjc2g9sbdPMABWnAWdJegaYTzqquKRDlAz+MQ64XtJ82LR38AOSARpmA5c3s8fQgHeBLWv/RbILfCHJMbVC9b27H5CM5DsvDZrFJOMvTiE5njhP0jrgVySj80wG7pO0LCLGSPoOMIOkN3hvK4PETgP6RsSCgmn/Q7L79CLJSDY7kZxkAaiNiLNJjjE+UdBrtK0kIpo7ubTZWdyImE0zj6WIiF8Dv27Luj0ajJWFpC+QjLFY1AWrW3G9PweejogbCqbtBtwYEce28LlrgLsi4uESlGkl4l1gKzlJJwE/BK4v8XrnAAcBNxdOj4hlwK9auhCa5Gyyw6+TcQ/QzHLLPUAzyy0HoJnllgPQzHLLAWhmueUANLPccgCaWW79f70Yc2vV9GFrAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This is a really simple code and this should be fairly easy to change if needed</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>4.9 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I think the N-body code is refering to the calculate trajectories function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="c1">#I am convertining it to seconds</span>
<span class="n">KepDt</span><span class="o">=</span> <span class="mf">0.5</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span>
<span class="n">TimeK</span> <span class="o">=</span> <span class="mi">500</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span>

<span class="n">KepPos</span><span class="p">,</span><span class="n">KepVel</span><span class="p">,</span><span class="n">KepTime</span> <span class="o">=</span> <span class="n">calculateTrajectories</span><span class="p">(</span><span class="n">MassKep</span><span class="p">,</span><span class="n">KepP</span><span class="p">,</span> <span class="n">KepV</span> <span class="p">,</span> <span class="n">KepDt</span><span class="p">,</span> <span class="n">TimeK</span><span class="p">)</span>

<span class="n">TimeKep</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">KepTime</span><span class="p">)</span><span class="o">/</span><span class="mi">24</span><span class="o">/</span><span class="mi">60</span><span class="o">/</span><span class="mi">60</span>
<span class="n">VelKep</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">KepVel</span><span class="p">)</span>
<span class="n">PosKep</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">KepPos</span><span class="p">)</span><span class="o">/</span><span class="n">au</span> <span class="c1">#I&#39;m just trying to fix my units.</span>

<span class="n">TimeKep</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(1001,)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>4.10 )</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Kepx</span> <span class="o">=</span> <span class="n">PosKep</span><span class="p">[:,</span><span class="mi">0</span><span class="p">,:]</span>
<span class="n">Kepy</span><span class="o">=</span> <span class="n">PosKep</span><span class="p">[:,</span><span class="mi">1</span><span class="p">,:]</span>
<span class="n">Kepz</span> <span class="o">=</span> <span class="n">PosKep</span><span class="p">[:,</span><span class="mi">2</span><span class="p">,:]</span>

<span class="n">x</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Kepx</span><span class="p">)</span>
<span class="n">y</span><span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Kepy</span><span class="p">)</span>
<span class="n">z</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">Kepz</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">size</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">y</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>3003
(1001, 3)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">mpl_toolkits</span> <span class="kn">import</span> <span class="n">mplot3d</span>
<span class="kn">import</span> <span class="nn">matplotlib.animation</span> <span class="k">as</span> <span class="nn">ani</span>
<span class="n">FFMpegWriter</span> <span class="o">=</span> <span class="n">ani</span><span class="o">.</span><span class="n">writers</span><span class="p">[</span><span class="s1">&#39;ffmpeg&#39;</span><span class="p">]</span>
<span class="n">writer</span> <span class="o">=</span> <span class="n">FFMpegWriter</span><span class="p">(</span><span class="n">fps</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>

<span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">fig</span><span class="o">.</span><span class="n">patch</span><span class="o">.</span><span class="n">set_alpha</span><span class="p">(</span><span class="mf">1.0</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">axes</span><span class="p">(</span><span class="n">projection</span><span class="o">=</span><span class="s1">&#39;3d&#39;</span><span class="p">)</span>

<span class="c1"># write plots to frames of a movie</span>
<span class="k">with</span> <span class="n">writer</span><span class="o">.</span><span class="n">saving</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="s2">&quot;Kepler16_3D.mp4&quot;</span><span class="p">,</span> <span class="mi">200</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">TimeKep</span><span class="p">),</span><span class="mi">5</span><span class="p">):</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">cla</span><span class="p">()</span>
        <span class="c1">#ax.view_init(0, 45) </span>
        

        <span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="n">i</span><span class="p">,:],</span><span class="n">y</span><span class="p">[</span><span class="n">i</span><span class="p">,:],</span><span class="n">z</span><span class="p">[</span><span class="n">i</span><span class="p">,:])</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_zlim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>        
        <span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;x (AU)&#39;</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;y (AU)&#39;</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_zlabel</span><span class="p">(</span><span class="s1">&#39;z (AU)&#39;</span><span class="p">)</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;Kepler16 system: day </span><span class="si">{</span><span class="n">TimeKep</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
        
                
        <span class="n">writer</span><span class="o">.</span><span class="n">grab_frame</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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hndxpFiOD/u0traiubkZMpkM77zzDvLy8mzW0L1HMj8/v6vKiOUTnAs4WomMbSZ4++23o7i42JunOCJRq9V49dVXce+99+LAgQPw8/MDj8dDW1sbAPsW46sNn+BcwN6N0V8zwfz8fKxZswZ33nmnl87OcbxdOTskJAR///vfsW7dOmzfvh2HDh3C7t278fTTT0OpVF5VI1l/jGjBmc1mFBUVAcCQC+q4E0ebCbLFeubNmweTyQSlUunV8xyMjIwMfPXVVwM6pdnirkeOHEFJSQl27tyJkpISl48pkUhw++234/3338d9992HVatWISQkhM4QrvZRbkQLzmg0Yvny5Th//jwEAgHy8/P7bMP+QCaTyWvn5UglstbWVnpuZ8+eBcMwCA0N9do5OsKECRMGbdzhqfVqZGQk4uLisGHDBqSmpuLf//43gKs/6GBEC04kEuH+++/Hd999h127duGuu+7Czz//bLMNh8OBwWDA6tWrsW/fPq+clyPuhr179yIjIwNZWVl4/PHHsWvXrlF5M3mycjb7QEpNTUVVVRWtpHw1M2JjKdnYufj4eKxZswZLly7FJ598ghkzZthsZzabsX79ekycOBGzZ8+mr1+8eBHff/89Hn74YY/UYZw3bx6NrmBZtWoV/f/q1auxevVql/a9cuVKHDp0CBEREXRKbQ1xoiHGSK6czbYEk0gk2Lhxo1vLro9Yhs0h4QA//vgj+d3vfkc4HA45e/aszXusb2bHjh1k7ty5xGg00ve0Wi2ZNWsW4XA4NiXWurq6vHPiQ+TkyZPkwoULJD093e777k4puummm/otV+dIxoUPxxmRU0qGYbB161asW7cO99xzD/74xz/SgFgW9in76aefYvHixbQ8eHd3N9577z0AwPr16+kCv7u7G5s2bcJrr73mxStxjVmzZiEkJKTf993VEMMRfJWz3cuIFByHw0FaWhr+8pe/4M4778SMGTOwZcsWALZTHLlcjpqaGtx99930tX/+859obGzEBx98ALlcDoVCAeCKJbGtrc2mY01FRQU++OADGjw7WnDXumrfvn2Ii4vDTz/9hPnz5+M3v/kNANtg5P7Wqz5cY0Su4TgcDn71q1/Rv3NyctDd3Y3Ozk4EBQXR9d2JEycQGhqK4OBgAFdqz//rX//CpUuXEBkZiaqqKjz++OMAgOrqami1Wtxwww10v3v37kVRUREeeugh5ObmQqvVYvny5d69WBcgblpXLVq0CIsWLerzekxMDHJzc+nf9tarPlxjRAoOsG2yl5WVhaysLPoeG/5z6dIl3HHHHQCACxcu4LPPPoNOp8P8+fMxfvx4hISEoLGxERMmTEBVVRUCAwNtmgOePXuWCqyrq4tOy8gIb/DnSykavYzIKSVg+8Tu/URn3/vVr35F/79q1SqEh4ejpaUFO3bswOTJk3HmzBkYjUbo9XrU1dXZiK2iogIdHR3Izs4GAFx//fX46aef0NPTM6LFBlxJBP3kk09ACMHPP/8MiURyzWaojzZG7AhnTX8CiI+PpyUBNmzYgOuuuw6BgYFITU3FunXrsHPnTkRERMDPzw/l5eVYsmQJ/ezhw4cxfvx4Wibg7NmzUCqV8Pf3B8Mww5oOsmzZMpw4cQJKpRJxcXF46aWXqGN/1apVmDdvHnJzc5GSkgKRSIRt27YN27n6cI4RWXnZUfR6PRQKBcaMGdPnPa1Wi5dffhmZmZlYtGgRZs6cifPnz8Pf3x8AcMstt2D16tVYuHAheDweVq9ejejoaDz//PMjfkrpY/QyKka4/ggICLArNuBKQ5A33ngDGo0GQUFBWLlyJWbPno158+YhMDAQra2tWLx4Md2+qKgId911F4CrP7zIx/AxYtdwQ4UduNkKUE888QRef/11WqDmyJEjdNvDhw/DYDDgxhtv9P6J+rimGNVTSndQW1uLV199FZMnT8Yjjzzim0768CijekrpLOyzhRUUIQT//Oc/cf3111ODik9sPjzJNT3CdXR04NSpU/if//mf4T4VH9cI17TgfPjwNlet0cSHj5GIT3A+fHgRn+B8+PAiPsH58OFFfILz4cOL/H8+FJ3p56BDIAAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">Video</span>
<span class="n">Video</span><span class="p">(</span><span class="s2">&quot;Kepler16_3D.mp4&quot;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="c1">#I embeded the code by using embeded</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[23]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<video controls  >
 <source src="data:video/mp4;base64,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AAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABAAAAAACAAABAAAAABxzdHNjAAAAAAAAAAEAAAABAAAAyQAAAAEAAAM4c3RzegAAAAAAAAAAAAAAyQAAW60AAAKRAAAA/wAAALkAAAIEAAABCQAAASUAAADRAAABagAAAJAAAAElAAABIQAAAVAAAACcAAABFwAAARQAAADkAAAAhAAAAREAAAEGAAABFwAAAIYAAAEfAAABBQAAAUYAAACPAAAA7wAAAPQAAAFcAAAAkAAAAP0AAAD2AAABOwAAAJgAAAEfAAAA/AAAATUAAAB7AAABGQAAAQgAAAHmAAAA6QAAAR0AAAEIAAABQQAAAQoAAAEWAAAAaAAAAOsAAAD8AAABiQAAAJ0AAAEEAAABHAAAATEAAAB+AAAA7QAAAQsAAAEHAAAAfAAAAO0AAAD2AAABCQAAAGMAAADrAAAA9QAAAXEAAACBAAABFAAAAPoAAAFxAAAAhAAAAOoAAAEOAAABRQAAAIsAAADnAAABBQAAAdcAAABiAAAA5AAAAPgAAAD6AAAAWwAAAOAAAAD6AAABZQAAAIUAAAD+AAABGwAAAPMAAAClAAABBAAAAR8AAAFhAAAAkAAAAQMAAAEFAAABFgAAAIAAAADvAAAA/gAAARoAAAByAAAA3AAAAQQAAAELAAAAhAAAAQMAAAEFAAABGAAAAJwAAAD1AAABDQAAAT8AAACKAAABDAAAAP8AAAHhAAAAeQAAAPAAAAEOAAAA8wAAAG4AAADoAAAA7AAAAS0AAACKAAAA+AAAAQsAAAE0AAAAqAAAARAAAAEFAAABOAAAAHIAAAEIAAABBgAAAP0AAABvAAAA5gAAAP8AAADPAAAAWwAAANsAAAECAAABBAAAAHoAAADxAAABEwAAAVMAAACuAAABAwAAAQQAAAEHAAAAiQAAAOwAAAEEAAABxQAAAHUAAADwAAAA6wAAAP8AAACEAAAA9AAAAREAAAFfAAAAcQAAAPwAAAEIAAABmwAAAHsAAAD9AAABDwAAAUoAAACMAAAA6gAAARYAAAE1AAAAYwAAAOoAAAD5AAABZAAAAHwAAADtAAAA+wAAAT4AAACZAAAA/QAAARUAAAD9AAAAfAAAAQAAAAEkAAABMQAAAHgAAADrAAAA/AAAAcgAAACmAAAAjQAAABRzdGNvAAAAAAAAAAEAAAAwAAAAYnVkdGEAAABabWV0YQAAAAAAAAAhaGRscgAAAAAAAAAAbWRpcmFwcGwAAAAAAAAAAAAAAAAtaWxzdAAAACWpdG9vAAAAHWRhdGEAAAABAAAAAExhdmY1OC4yOS4xMDA=" type="video/mp4">
 Your browser does not support the video tag.
 </video>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="5.-choose-your-own-adventure">5. choose your own adventure<a class="anchor-link" href="#5.-choose-your-own-adventure">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Most of this section will be trying to read over these files and experimenting to see what I can do with these trajectories and seeing what can give me the most information.</p>
<p>then after that I will then create a move so that we can see the path of these trajectories. I feel like most of this work will come from the most recent lectrues</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#loads the file into this notebook</span>
<span class="n">files</span> <span class="o">=</span><span class="s1">&#39;/home/vees3978/Final_Project_2600/&#39;</span> <span class="c1">#I should make sure to pay attention to what folder I downloaded it to</span>

<span class="c1">#this takes the files from each file</span>
<span class="n">pltDisk</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;planetesimalDisk.txt&#39;</span><span class="p">,</span><span class="n">sep</span><span class="o">=</span><span class="s1">&#39; &#39;</span><span class="p">,</span> <span class="n">skiprows</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">names</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mass (kg)&quot;</span><span class="p">,</span> <span class="s2">&quot;x(m)&quot;</span><span class="p">,</span><span class="s2">&quot;y(m)&quot;</span><span class="p">,</span><span class="s2">&quot;z (m)&quot;</span><span class="p">,</span><span class="s2">&quot;vx (m/s)&quot;</span><span class="p">,</span> <span class="s2">&quot;vy (m/s)&quot;</span><span class="p">,</span><span class="s2">&quot;vz (m/s)&quot;</span><span class="p">])</span>

<span class="n">pltMass</span><span class="o">=</span> <span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;mass (kg)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span> 
<span class="n">pltx</span><span class="o">=</span> <span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;x(m)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="n">plty</span><span class="o">=</span><span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;y(m)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="n">pltz</span><span class="o">=</span><span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;z (m)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="n">pltvx</span><span class="o">=</span><span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;vx (m/s)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="n">pltvy</span><span class="o">=</span><span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;vy (m/s)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>
<span class="n">pltvz</span><span class="o">=</span><span class="n">pltDisk</span><span class="p">[</span><span class="s2">&quot;vz (m/s)&quot;</span><span class="p">]</span><span class="o">.</span><span class="n">values</span>


    
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">totpltpos</span><span class="o">=</span> <span class="p">[]</span>
<span class="n">totpltvel</span><span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">pltMass</span><span class="p">)):</span>
    <span class="n">totpltpos</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">pltx</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="n">plty</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="n">pltz</span><span class="p">[</span><span class="n">i</span><span class="p">]]))</span>
    <span class="n">totpltvel</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">pltvx</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="n">pltvy</span><span class="p">[</span><span class="n">i</span><span class="p">],</span><span class="n">pltvz</span><span class="p">[</span><span class="n">i</span><span class="p">]]))</span>
    
<span class="n">pltdt</span><span class="o">=</span><span class="mf">0.5</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span>
<span class="n">pltT</span><span class="o">=</span><span class="mi">350</span><span class="o">*</span><span class="mi">24</span><span class="o">*</span><span class="mi">60</span><span class="o">*</span><span class="mi">60</span>    
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">PDP</span><span class="p">,</span><span class="n">PDV</span><span class="p">,</span><span class="n">PDT</span> <span class="o">=</span> <span class="n">calculateTrajectories</span><span class="p">(</span><span class="n">pltMass</span><span class="p">,</span><span class="n">totpltpos</span><span class="p">,</span> <span class="n">totpltvel</span> <span class="p">,</span> <span class="n">pltdt</span><span class="p">,</span> <span class="n">pltT</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I am sorry that this is so incomplete. I am just really stuck on the function. Most of this project relies on this function so I am just really trying to understand the best way to make this work!</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">TimepltD</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">PDT</span><span class="p">)</span><span class="o">/</span><span class="mi">24</span><span class="o">/</span><span class="mi">60</span><span class="o">/</span><span class="mi">60</span>
<span class="n">VelpltD</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">PDV</span><span class="p">)</span>
<span class="n">PosPltD</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(</span><span class="n">PDP</span><span class="p">)</span><span class="o">/</span><span class="n">au</span>

<span class="n">PosPltD</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[27]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>(701, 30, 3)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">PDPx</span> <span class="o">=</span> <span class="n">PosPltD</span><span class="p">[:,:,</span><span class="mi">0</span><span class="p">]</span>
<span class="n">PDPy</span> <span class="o">=</span> <span class="n">PosPltD</span><span class="p">[:,:,</span><span class="mi">1</span><span class="p">]</span>
<span class="n">PDPz</span> <span class="o">=</span> <span class="n">PosPltD</span><span class="p">[:,:,</span><span class="mi">2</span><span class="p">]</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#I was going to scale it but it looked bad. the points were really small</span>
<span class="c1">#pltDpor=[]</span>
<span class="c1">#for i in range(len(pltMass)):</span>
    <span class="c1">#pltDpor.append([i]/np.max(pltMass)*100)</span>

<span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span>
<span class="n">fig</span><span class="o">.</span><span class="n">patch</span><span class="o">.</span><span class="n">set_alpha</span><span class="p">(</span><span class="mf">1.0</span><span class="p">)</span>
<span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">axes</span><span class="p">(</span><span class="n">projection</span><span class="o">=</span><span class="s1">&#39;3d&#39;</span><span class="p">)</span>

<span class="c1"># write plots to frames of a movie</span>
<span class="k">with</span> <span class="n">writer</span><span class="o">.</span><span class="n">saving</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="s2">&quot;planetesimalDisk.mp4&quot;</span><span class="p">,</span> <span class="mi">200</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">TimepltD</span><span class="p">),</span><span class="mi">5</span><span class="p">):</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">cla</span><span class="p">()</span>
        <span class="c1">#ax.view_init(0, 45) </span>
        

        <span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">PDPx</span><span class="p">[</span><span class="n">i</span><span class="p">,:],</span><span class="n">PDPy</span><span class="p">[</span><span class="n">i</span><span class="p">,:],</span><span class="n">PDPz</span><span class="p">[</span><span class="n">i</span><span class="p">,:])</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_zlim</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>        
        <span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;x (AU)&#39;</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;y (AU)&#39;</span><span class="p">);</span> <span class="n">ax</span><span class="o">.</span><span class="n">set_zlabel</span><span class="p">(</span><span class="s1">&#39;z (AU)&#39;</span><span class="p">)</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;planetesimalDisk: day </span><span class="si">{</span><span class="n">TimepltD</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
        
                
        <span class="n">writer</span><span class="o">.</span><span class="n">grab_frame</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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yMjIwHvvvYf//e9/+OCDD/wWvTJafOS5Uj8yUIzLD5ednT3qNudrCE9UVBTWrFmDNWvWQKfTYd++fdi8eTOam5tx9dVXY8mSJaAoCnV1dWznoKioKHA4HLbE+3C92QIFI/Jp06bho48+wldffYWPPvrIb2JzOp34f//v/7k9XJcuXer2Wx88eBB1dXWoq6vD0aNHce+99467fuRY+sefLQJuihqufNn5hFwux2233YZPPvkE3377LWbNmoW//e1vuPPOO7Fv3z7o9XpoNBocPXoUJSUlOHbsGNLS0oIqNrvdzjZg3L9/Pw4cOIDdu3f7pfYmg+vDVSAQsA9XV4arH+krJSUlbL8KiqK8nsafbUYd4RYsWIDu7u4hrz///PNYtmzZqAc4V8qX+QupVIqVK1di5cqVMJlMOHToELZv346ysjIUFRXBaDRiw4YNaGhoQGdnJ+Li4hAdHR3Q+ifMWnHKlCn47LPPWN+jv+MwvYmP9Ef9yO7ubmzcuBGzZs1Cb28vtm7des64MUb9lb/44otxHeBcKV8WCCQSCVasWIEVK1agtrYW1157LfLz83HXXXfhkksuwbJlyyCRSNDS0gKhUMj6xvwZ1cJYQVNTU3HkyBG8++67OHDgQEAKwnrzcB3vA7isrAz5+fn48MMPYbVa8cADD2DhwoX461//6tUS52wT8MfC7NmzUVdXh6amJthsNrz33nsBr/A0EUlMTMSnn36Kjz/+GKdPn8YNN9yATz75BKtWrcK///1vqFQq9Pf34/Tp0zh16hTa29ths9nGdUyHw4HTp09j8uTJ+P777/HWW29h7969AWuY4s3DdTwP4MrKStx2223YuXMn+Hw+oqKi8O6772LWrFl4+OGH0draCgATe3pJxsFHH31EEhMTiUAgILGxsWThwoWEEEI6OjrItddey2534MABMm3aNJKWlkaee+65Uffb29tLFixYQKZOnUoWLFhANBqNx+1SUlJIXl4eKSgoILNmzRrPpZw17HY7+fLLL8natWtJbm4uufXWW8mHH35ISktLyZEjR8g333xDqquriUajIf39/V7/0+v15Ouvvyb19fXkgw8+IPPmzRv2e/TntUyZMoU0NjYSq9VK8vPzSXl5uds2+/fvJ4sWLSI0TZMffviBzJ4926djfPLJJ+TKK68k//nPf4jBYGBff+ihh8jcuXOJw+Hwy7UEinEJLlD8/ve/Jy+++CIhhJAXX3yRPPzwwx63S0lJISqVKpinFlAcDgf5+uuvyfr160leXh65+eabya5du0hpaSn5+uuvyddff02qqqpIb2/vqGL75ptvSF1dHfn444/JnDlziFqtDso1eHq4bt26lWzdupUQQghN0+S+++4jaWlpJC8vjxw/fnzUfba2tg45xuWXX0527NhBrFYr+/r69evJa6+95ser8T8TUnAZGRmks7OTEEJIZ2cnycjI8Ljd+SY4V5xOJ/nhhx/Igw8+SKZPn05WrFhB/v3vf5PS0lLyzTffkCNHjpCKigqiUqmGiO3bb78ltbW1ZP/+/aSoqIj09PSc7csZMydPniS33HIL+fzzz91eP3z4MLnkkkvInj172Nc+//xz9kE9UZmQoV1yuRw6nY79W6FQQKvVDtluypQpUCgUoCgK99xzD+6+++4gnmXwoGkap0+fxu7du3Ho0CEkJyfj+uuvR1FREfR6PRwOB6KjoxETE4P6+nrExMSgqakJjz322Dlfxq6hoQF79+5FbW0tli9fjoULF7Lv7du3D+vXr8ePP/6ISZMmwWAw4B//+AdWrVo1Ya/5rAluJHfD6tWrvRJcZ2cnEhISoFQqcfXVV+P111/HZZddFsjTPuuQn3L6PvzwQxQXFyMmJgbXX389Zs2ahfr6eqjVavzwww84efIkvvjiCyQlJZ3tUx43TU1NOHDgAMrKyrB8+XJce+217Ht33HEHXnnlFbaNtNPpnNDB1xNyhMvMzMSRI0cQHx+Prq4uXH755aipqRnxM08//TTCw8Px0EMPBekszz6EEFRXV+P999/Htm3bkJmZiVmzZuHrr79GfHw8JBIJPvjgg7N9mj6zfft2KJVKXHfddWyUSktLC/bv34/S0lJccsklWL16NR5++GFUVVVh3759Z/mMfeDszWaH56GHHnIzmvz+978fso3RaCR6vZ79/7x588jBgweDep4TheLiYrJp0yZSV1dHVq5cSb777jtCyICBwp8Ew3psNpvJqlWrSEJCAvn9739PbrjhBqJUKondbif9/f1k9+7dJC8vj9x4441k4cKFrFXS6XSO+/qCwYQUnFqtJldeeSWZOnUqufLKK0lvby8hxN3d0NDQQPLz80l+fj7Jycnxyt0QYnwE0nrs+nDYs2cPSUtLIyUlJeS3v/0tueOOO8i6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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">Video</span>
<span class="n">Video</span><span class="p">(</span><span class="s2">&quot;planetesimalDisk.mp4&quot;</span><span class="p">,</span> <span class="n">embed</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[30]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<video controls  >
 <source src="data:video/mp4;base64,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AAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAADAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAAAEAAAMAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAMAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAMAAAAAAQAAAQAAAAABAAADAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAADAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAADAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAABQAAAAABAAACAAAAAAEAAAAAAAAAAQAAAQAAAAABAAAFAAAAAAEAAAIAAAAAAQAAAAAAAAABAAABAAAAAAEAAAUAAAAAAQAAAgAAAAABAAAAAAAAAAEAAAEAAAAAAQAAAwAAAAABAAABAAAAABxzdHNjAAAAAAAAAAEAAAABAAAAjQAAAAEAAAJIc3RzegAAAAAAAAAAAAAAjQAAW8cAAAkbAAADnQAAAvYAAALTAAAEUgAAAu0AAAWCAAAC4wAAArYAAALiAAAEfQAAAsAAAARdAAACoQAABQUAAALCAAAE3gAAAu4AAAKiAAACoAAABAwAAAKrAAAFdwAAAyYAAAKWAAACxwAABI4AAALVAAAD3QAAAnsAAASmAAACvgAABbMAAAM7AAACwwAAAuMAAASzAAAC6wAABw8AAANJAAADCQAAAsMAAAUxAAADBQAAAtwAAALvAAAFAAAAAyoAAALmAAAClAAABWQAAAOLAAACsgAAAzcAAAWwAAADMQAAAxYAAALQAAAFYwAAA4oAAALiAAACwgAABXwAAAMyAAACyQAAAt8AAAUWAAADFwAAAr4AAAK7AAAEzAAAAqoAAAR0AAAC5AAABREAAAMuAAACsQAAAuUAAAXRAAADPQAAArIAAALWAAAE8AAAAtcAAAMEAAACwwAABT8AAAMrAAACxQAAAscAAARvAAAC3wAABVUAAALPAAACxQAAAs0AAAUJAAADJQAAAvEAAAKuAAAFGAAAAwcAAALCAAACsQAABTcAAAMeAAAC1QAAAxcAAAYaAAADOgAAAv4AAALDAAAEgAAAAr4AAAXGAAADEgAAAoQAAALaAAAF/AAAAz0AAALpAAAC5QAABWQAAAL9AAACyAAAAs0AAAStAAADAAAAArQAAAKbAAAE5QAAA0wAAALtAAACjQAABRUAAAKtAAACewAAAtAAAAM4AAAC8QAAABRzdGNvAAAAAAAAAAEAAAAwAAAAYnVkdGEAAABabWV0YQAAAAAAAAAhaGRscgAAAAAAAAAAbWRpcmFwcGwAAAAAAAAAAAAAAAAtaWxzdAAAACWpdG9vAAAAHWRhdGEAAAABAAAAAExhdmY1OC4yOS4xMDA=" type="video/mp4">
 Your browser does not support the video tag.
 </video>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#print(PDPx.shape)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
