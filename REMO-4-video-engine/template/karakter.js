// Generator SVG karakter untuk REMO 4 (diwarisi dari REMO 3, MIT — Weyeni.id).
// Tokoh host (cowok dewasa) & lina (cewek dewasa): artwork baru dari GPT, 3 Nov 2026.
// File sumber: master-aset/karakter-svg/baru/cowok-dewasa.svg, cewek-dewasa.svg.
// nur / yohana / togar tetap memakai generator lama (diwarisi REMO 3).
(function () {
  const LOOKS = {
    host: { skin: '#C2805A', shade: '#A86A47', top: '#D9483B', shirt: '#FFF6EC', seam: '#B8382D', bottom: '#2E3A5C' },
    nur: { skin: '#C98B62', shade: '#AD7350', top: '#E9A23B', shirt: '#FFF6EC', seam: '#C9862A', bottom: '#2E3A5C' },
    yohana: { skin: '#7A4A30', shade: '#643B25', top: '#4A6FA5', shirt: '#FFF6EC', seam: '#3A5A88', bottom: '#2E3A5C' },
    togar: { skin: '#B07650', shade: '#94603F', top: '#A9C2DA', shirt: '#FFFFFF', seam: '#86A3BF', bottom: '#4A3F35' },
    lina: { skin: '#E2B48C', shade: '#C99A72', top: '#7B5EA7', shirt: '#FFF6EC', seam: '#634A8A', bottom: '#2E3A5C' }
  };
  const BROWS = {
    normal: ['M112 126 Q124 120 136 126', 'M164 126 Q176 120 188 126'],
    kaget: ['M112 114 Q124 106 136 112', 'M164 112 Q176 106 188 114'],
    berpikir: ['M112 128 Q124 126 136 128', 'M164 118 Q176 110 188 118']
  };
  const MOUTHS = {
    senyum: { d: 'M132 178 Q150 194 168 178', fill: 'none' },
    bicara: { d: 'M134 177 Q150 202 166 177 Z', fill: '#7A2E2E' },
    kaget: { d: 'M141 188 a9 11 0 1 0 18 0 a9 11 0 1 0 -18 0 Z', fill: '#7A2E2E' },
    berpikir: { d: 'M138 184 Q146 178 152 183 Q158 188 164 182', fill: 'none' }
  };
  const RIGHTS = {
    santai: { d: 'M202 242 Q218 278 220 310', x: 220, y: 318 },
    'pegang-hp': { d: 'M202 246 Q228 280 206 296', x: 200, y: 298 },
    kaget: { d: 'M202 242 Q228 222 228 198', x: 228, y: 190 },
    berpikir: { d: 'M202 246 Q222 222 186 210', x: 180, y: 208 },
    menunjuk: { d: 'M202 244 Q236 224 254 194', x: 258, y: 188 }
  };
  const L_DOWN = { d: 'M98 242 Q82 278 80 310', x: 80, y: 318 };
  const L_UP = { d: 'M98 242 Q72 222 72 198', x: 72, y: 190 };

  // Artwork baru (GPT, 3 Nov 2026): mulut/alis dinamis, kedip, pose via rotasi lengan.
  // Mulut bicara/kaget/berpikir memakai koordinat mulut baru (sekitar x 137-163, y 170-199).
  const NEW_MOUTH = {
    senyum: { d: 'M137 170 Q150 182 163 170', fill: 'none' },
    bicara: { d: 'M134 177 Q150 202 166 177 Z', fill: '#7A2E2E' },
    kaget: { d: 'M141 188 a9 11 0 1 0 18 0 a9 11 0 1 0 -18 0 Z', fill: '#7A2E2E' },
    berpikir: { d: 'M138 184 Q146 178 152 183 Q158 188 164 182', fill: 'none' }
  };
  const NEW_ART = {
    host: {
      skin: "#C2805A",
      hair: "<g id=\"hair\" fill=\"#241F1E\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M80 133 Q72 85 102 62 Q125 43 153 49 Q183 43 204 66 Q229 91 220 135 L205 119 Q190 108 179 94 Q155 107 126 96 Q104 111 83 135 Z\"/> <path d=\"M112 64 Q108 43 126 38 Q133 34 139 44 Q149 26 160 38 Q166 29 174 41 Q186 41 184 58 Q167 51 157 61 Q140 51 128 66 Z\"/> </g>",
      head: "<g id=\"head\"> <circle cx=\"150\" cy=\"140\" r=\"72\" fill=\"#C2805A\" stroke=\"#241F1E\" stroke-width=\"4\"/> <path d=\"M80 112 Q79 79 105 62 Q126 48 151 53 Q185 45 207 75 Q218 91 220 116 Q200 97 183 89 Q157 103 126 94 Q103 108 80 112 Z\" fill=\"#241F1E\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"/> <path d=\"M79 142 Q68 138 70 153 Q72 165 84 163\" fill=\"#C2805A\" stroke=\"#241F1E\" stroke-width=\"3\"/> <path d=\"M221 142 Q232 138 230 153 Q228 165 216 163\" fill=\"#C2805A\" stroke=\"#241F1E\" stroke-width=\"3\"/> </g>",
      eyesAttrs: " fill=\"#FFFFFF\" stroke=\"#241F1E\" stroke-width=\"3\"",
      eyesInner: " <ellipse cx=\"124\" cy=\"140\" rx=\"9\" ry=\"12\"/> <ellipse cx=\"176\" cy=\"140\" rx=\"9\" ry=\"12\"/> <ellipse cx=\"125\" cy=\"142\" rx=\"4.5\" ry=\"7\" fill=\"#241F1E\" stroke=\"none\"/> <ellipse cx=\"177\" cy=\"142\" rx=\"4.5\" ry=\"7\" fill=\"#241F1E\" stroke=\"none\"/> <circle cx=\"126.5\" cy=\"139\" r=\"2\" fill=\"#FFFFFF\" stroke=\"none\"/> <circle cx=\"178.5\" cy=\"139\" r=\"2\" fill=\"#FFFFFF\" stroke=\"none\"/> ",
      body: "<g id=\"body\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M126 205 L110 214 L100 274 L200 274 L190 214 L174 205 Z\" fill=\"#FFF6EC\"/> <path d=\"M117 207 Q103 211 98 226 L89 292 L108 302 L123 248 L128 228 Z\" fill=\"#D9483B\"/> <path d=\"M183 207 Q197 211 202 226 L211 292 L192 302 L177 248 L172 228 Z\" fill=\"#D9483B\"/> <path d=\"M126 205 Q150 225 174 205 L190 215 L199 292 L101 292 L110 215 Z\" fill=\"#D9483B\"/> <path d=\"M132 211 Q150 230 168 211 L163 239 L150 249 L137 239 Z\" fill=\"#FFF6EC\"/> <path d=\"M101 283 L199 283 L204 309 L96 309 Z\" fill=\"#2E3A5C\"/> </g>",
      armLAttrs: " stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"",
      armLInner: " <path d=\"M101 221 Q91 225 88 241 L77 294 Q73 309 81 313 Q89 317 95 303 L111 253 L115 232 Z\" fill=\"#D9483B\"/> <path d=\"M77 294 Q69 309 77 322 Q83 329 91 320 L96 306 Q89 313 81 313 Z\" fill=\"#C2805A\"/> ",
      armRAttrs: " stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"",
      armRInner: " <path d=\"M199 221 Q209 225 212 241 L223 294 Q227 309 219 313 Q211 317 205 303 L189 253 L185 232 Z\" fill=\"#D9483B\"/> <path d=\"M223 294 Q231 309 223 322 Q217 329 209 320 L204 306 Q211 313 219 313 Z\" fill=\"#C2805A\"/> ",
      legs: "<g id=\"legs\" fill=\"#2E3A5C\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M99 304 L150 304 L148 376 L143 397 L113 397 L110 376 Z\"/> <path d=\"M150 304 L201 304 L190 376 L187 397 L157 397 L152 376 Z\"/> <path d=\"M150 309 L150 376\" fill=\"none\"/> </g>",
      shoes: "<g id=\"shoes\" fill=\"#1F2433\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M113 383 L143 383 L147 396 Q155 402 151 409 L103 409 Q99 405 104 397 Z\"/> <path d=\"M157 383 L187 383 L196 397 Q201 405 196 409 L149 409 Q145 402 153 396 Z\"/> <path d=\"M104 403 Q126 406 151 403\" fill=\"none\" stroke-width=\"2.5\"/> <path d=\"M150 403 Q174 406 196 403\" fill=\"none\" stroke-width=\"2.5\"/> </g>",
    },
    lina: {
      skin: "#E2B48C",
      hair: "<g id=\"hair\" fill=\"#1B1717\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M78 139 Q65 83 103 57 Q150 23 197 57 Q235 83 222 139 L222 245 Q218 263 201 263 L99 263 Q82 263 78 245 Z\"/> <path d=\"M83 102 Q67 157 79 221 L83 251 Q89 263 101 260 L105 112 Z\"/> <path d=\"M217 102 Q233 157 221 221 L217 251 Q211 263 199 260 L195 112 Z\"/> </g>",
      head: "<g id=\"head\"> <circle cx=\"150\" cy=\"140\" r=\"72\" fill=\"#E2B48C\" stroke=\"#241F1E\" stroke-width=\"4\"/> <path d=\"M81 119 Q79 61 126 53 Q164 42 197 68 Q215 85 219 117 Q204 91 184 83 Q153 105 107 89 Q96 101 81 119 Z\" fill=\"#1B1717\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"/> <path d=\"M79 125 Q77 166 91 180\" fill=\"none\" stroke=\"#241F1E\" stroke-width=\"3\"/> <path d=\"M221 125 Q223 166 209 180\" fill=\"none\" stroke=\"#241F1E\" stroke-width=\"3\"/> <path d=\"M79 143 Q68 139 70 153 Q72 166 84 163\" fill=\"#E2B48C\" stroke=\"#241F1E\" stroke-width=\"3\"/> <path d=\"M221 143 Q232 139 230 153 Q228 166 216 163\" fill=\"#E2B48C\" stroke=\"#241F1E\" stroke-width=\"3\"/> </g>",
      eyesAttrs: " fill=\"#FFFFFF\" stroke=\"#241F1E\" stroke-width=\"3\"",
      eyesInner: " <ellipse cx=\"124\" cy=\"140\" rx=\"9\" ry=\"12\"/> <ellipse cx=\"176\" cy=\"140\" rx=\"9\" ry=\"12\"/> <ellipse cx=\"125\" cy=\"142\" rx=\"4.5\" ry=\"7\" fill=\"#241F1E\" stroke=\"none\"/> <ellipse cx=\"177\" cy=\"142\" rx=\"4.5\" ry=\"7\" fill=\"#241F1E\" stroke=\"none\"/> <circle cx=\"126.5\" cy=\"139\" r=\"2\" fill=\"#FFFFFF\" stroke=\"none\"/> <circle cx=\"178.5\" cy=\"139\" r=\"2\" fill=\"#FFFFFF\" stroke=\"none\"/> ",
      body: "<g id=\"body\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M126 205 L110 214 L100 274 L200 274 L190 214 L174 205 Z\" fill=\"#FFF6EC\"/> <path d=\"M117 207 Q103 211 98 226 L89 292 L108 302 L123 248 L128 228 Z\" fill=\"#7B5EA7\"/> <path d=\"M183 207 Q197 211 202 226 L211 292 L192 302 L177 248 L172 228 Z\" fill=\"#7B5EA7\"/> <path d=\"M126 205 Q150 225 174 205 L190 215 L199 292 L101 292 L110 215 Z\" fill=\"#7B5EA7\"/> <path d=\"M132 211 Q150 230 168 211 L163 239 L150 249 L137 239 Z\" fill=\"#FFF6EC\"/> <path d=\"M101 283 L199 283 L204 309 L96 309 Z\" fill=\"#2E3A5C\"/> </g>",
      armLAttrs: " stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"",
      armLInner: " <path d=\"M101 221 Q91 225 88 241 L77 294 Q73 309 81 313 Q89 317 95 303 L111 253 L115 232 Z\" fill=\"#7B5EA7\"/> <path d=\"M77 294 Q69 309 77 322 Q83 329 91 320 L96 306 Q89 313 81 313 Z\" fill=\"#E2B48C\"/> ",
      armRAttrs: " stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"",
      armRInner: " <path d=\"M199 221 Q209 225 212 241 L223 294 Q227 309 219 313 Q211 317 205 303 L189 253 L185 232 Z\" fill=\"#7B5EA7\"/> <path d=\"M223 294 Q231 309 223 322 Q217 329 209 320 L204 306 Q211 313 219 313 Z\" fill=\"#E2B48C\"/> ",
      legs: "<g id=\"legs\" fill=\"#2E3A5C\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M99 304 L150 304 L148 376 L143 397 L113 397 L110 376 Z\"/> <path d=\"M150 304 L201 304 L190 376 L187 397 L157 397 L152 376 Z\"/> <path d=\"M150 309 L150 376\" fill=\"none\"/> </g>",
      shoes: "<g id=\"shoes\" fill=\"#1F2433\" stroke=\"#241F1E\" stroke-width=\"4\" stroke-linejoin=\"round\"> <path d=\"M113 383 L143 383 L147 396 Q155 402 151 409 L103 409 Q99 405 104 397 Z\"/> <path d=\"M157 383 L187 383 L196 397 Q201 405 196 409 L149 409 Q145 402 153 396 Z\"/> <path d=\"M104 403 Q126 406 151 403\" fill=\"none\" stroke-width=\"2.5\"/> <path d=\"M150 403 Q174 406 196 403\" fill=\"none\" stroke-width=\"2.5\"/> </g>",
    },
  };
  function newCharSVG(t, e, p, o) {
    const A = NEW_ART[t];
    const mk = o.mulut || e;
    const m = NEW_MOUTH[mk] || NEW_MOUTH.senyum;
    const b = e === 'kaget' ? BROWS.kaget : (e === 'berpikir' ? BROWS.berpikir : BROWS.normal);
    const blink = o.kedip ? ' transform="translate(0 140) scale(1 0.15) translate(0 -140)"' : '';
    let armL = '', armR = '', extra = '';
    if (p === 'pegang-hp') {
      armR = ' transform="rotate(55 200 225)"';
      extra = '<rect x="124" y="246" width="32" height="50" rx="6" fill="#1F2433"/><rect x="128" y="251" width="24" height="38" rx="3" fill="#F4B740"/>';
    } else if (p === 'kaget') {
      armL = ' transform="rotate(135 100 225)"';
      armR = ' transform="rotate(-135 200 225)"';
    } else if (p === 'berpikir') {
      armR = ' transform="rotate(112 200 225)"';
    } else if (p === 'menunjuk') {
      armR = ' transform="rotate(-135 200 225)"';
      extra = '<path d="M256 150 L270 134" fill="none" stroke="' + A.skin + '" stroke-width="9" stroke-linecap="round"/>';
    }
    return '<svg viewBox="0 0 300 420" width="100%" height="100%" aria-hidden="true">'
      + A.hair + A.head
      + '<g id="eyes"' + A.eyesAttrs + blink + '>' + A.eyesInner + '</g>'
      + '<g id="brows" fill="none" stroke="#241F1E" stroke-width="5" stroke-linecap="round"><path d="' + b[0] + '"/><path d="' + b[1] + '"/></g>'
      + '<g id="mouth"><path d="' + m.d + '" fill="' + m.fill + '" stroke="#1F2433" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'
      + A.body
      + '<g id="arm-left"' + A.armLAttrs + armL + '>' + A.armLInner + '</g>'
      + '<g id="arm-right"' + A.armRAttrs + armR + '>' + A.armRInner + '</g>'
      + A.legs + A.shoes + extra + '</svg>';
  }

  window.characterSVG = function (o) {
    const t = o.tokoh || 'host';
    if (NEW_ART[t]) return newCharSVG(t, o.ekspresi || 'senyum', o.pose || 'santai', o);
    const e = o.ekspresi || 'senyum', p = o.pose || 'santai';
    const k = LOOKS[t];
    const mouthKey = o.mulut || e;
    const b = e === 'kaget' ? BROWS.kaget : (e === 'berpikir' ? BROWS.berpikir : BROWS.normal);
    const m = MOUTHS[mouthKey] || MOUTHS.senyum;
    const r = RIGHTS[p] || RIGHTS.santai;
    const l = p === 'kaget' ? L_UP : L_DOWN;
    const eyeY = e === 'berpikir' ? 145 : 148;
    const eyeRy = o.kedip ? 1.6 : (e === 'kaget' ? 13 : 11);
    const show = (c) => (c ? '' : 'display:none');
    const blushL = t === 'nur' ? 116 : 106, blushR = t === 'nur' ? 184 : 194;
    return `<svg viewBox="0 0 300 420" width="100%" height="100%" aria-hidden="true">
<g style="${show(t !== 'nur')}"><rect x="102" y="324" width="42" height="64" rx="12" fill="${k.bottom}"/><rect x="156" y="324" width="42" height="64" rx="12" fill="${k.bottom}"/></g>
<path style="${show(t === 'nur')}" d="M100 326 L200 326 L214 386 Q214 392 208 392 L92 392 Q86 392 86 386 Z" fill="${k.bottom}"/>
<ellipse cx="120" cy="392" rx="28" ry="12" fill="#1F2433"/><ellipse cx="180" cy="392" rx="28" ry="12" fill="#1F2433"/>
<path d="M86 304 C86 252 108 222 150 222 C192 222 214 252 214 304 L214 334 Q214 340 208 340 L92 340 Q86 340 86 334 Z" fill="${k.top}"/>
<path d="M130 224 L150 266 L170 224 Z" fill="${k.shirt}"/>
<path d="M150 266 L150 338" fill="none" stroke="${k.seam}" stroke-width="3" stroke-linecap="round"/>

<path d="${l.d}" fill="none" stroke="${k.top}" stroke-width="26" stroke-linecap="round"/>
<path d="${r.d}" fill="none" stroke="${k.top}" stroke-width="26" stroke-linecap="round"/>
<path style="${show(t === 'lina')}" d="M74 150 C74 82 110 58 150 58 C190 58 226 82 226 150 L226 196 Q226 206 216 206 L84 206 Q74 206 74 196 Z" fill="#1B1717"/>
<rect x="138" y="200" width="24" height="26" rx="6" fill="${k.shade}"/>
<g style="${show(t !== 'nur')}"><circle cx="80" cy="150" r="14" fill="${k.skin}"/><circle cx="220" cy="150" r="14" fill="${k.skin}"/></g>
<circle cx="150" cy="140" r="72" fill="${k.skin}"/>
<g style="${show(t === 'host')}" fill="#241F1E"><path d="M78 134 C78 80 112 58 150 58 C196 58 224 86 224 130 C214 114 198 104 178 102 C186 112 186 120 182 126 C168 110 140 102 112 106 C98 110 86 120 78 134 Z"/><path d="M148 62 C156 42 174 36 188 42 C176 46 166 54 162 64 Z"/></g>
<ellipse cx="${blushL}" cy="172" rx="11" ry="6" fill="#E07B63" opacity=".5"/><ellipse cx="${blushR}" cy="172" rx="11" ry="6" fill="#E07B63" opacity=".5"/>
<path d="${b[0]}" fill="none" stroke="#241F1E" stroke-width="5" stroke-linecap="round"/><path d="${b[1]}" fill="none" stroke="#241F1E" stroke-width="5" stroke-linecap="round"/>
<ellipse cx="124" cy="${eyeY}" rx="8" ry="${eyeRy}" fill="#1F2433"/><ellipse cx="176" cy="${eyeY}" rx="8" ry="${eyeRy}" fill="#1F2433"/>
<g style="${show(!o.kedip)}"><circle cx="127" cy="${eyeY - 4}" r="3" fill="#fff"/><circle cx="179" cy="${eyeY - 4}" r="3" fill="#fff"/></g>
<path d="${m.d}" fill="${m.fill}" stroke="#1F2433" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<g style="${show(p === 'pegang-hp')}"><rect x="184" y="250" width="32" height="50" rx="6" fill="#1F2433"/><rect x="188" y="255" width="24" height="38" rx="3" fill="#F4B740"/></g>
<path style="${show(p === 'menunjuk')}" d="M262 180 L272 164" fill="none" stroke="${k.skin}" stroke-width="9" stroke-linecap="round"/>
<circle cx="${l.x}" cy="${l.y}" r="13" fill="${k.skin}"/><circle cx="${r.x}" cy="${r.y}" r="13" fill="${k.skin}"/>
</svg>`;
  };
})();
