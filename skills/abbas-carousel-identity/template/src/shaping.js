// Scoped shaping fix for IBM Plex Sans Arabic 1.101 (see base.css .rlig-off).
// Wraps each word where a tooth letter (ب ت ث ن ي ئ پ) is followed by alef maksura (ى),
// so only those words render without the ambiguous ligature; لا elsewhere is untouched.
(() => {
  const AFFECTED = /[بتثنيئپ][ً-ْ]*ى/;
  const WORD = /[؀-ۿݐ-ݿ]+/g;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) if (AFFECTED.test(walker.currentNode.nodeValue)) nodes.push(walker.currentNode);
  for (const node of nodes) {
    if (node.parentElement.closest('.rlig-off')) continue;
    const svgText = node.parentElement.closest('svg');
    const frag = document.createDocumentFragment();
    let last = 0;
    for (const m of node.nodeValue.matchAll(WORD)) {
      if (!AFFECTED.test(m[0])) continue;
      frag.append(node.nodeValue.slice(last, m.index));
      const el = svgText ? document.createElementNS('http://www.w3.org/2000/svg', 'tspan') : document.createElement('span');
      el.setAttribute('class', 'rlig-off');
      el.textContent = m[0];
      frag.append(el);
      last = m.index + m[0].length;
    }
    frag.append(node.nodeValue.slice(last));
    node.replaceWith(frag);
  }
})();
