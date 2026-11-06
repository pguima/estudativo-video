/*!
 * Cena de teste: a família inteira no mesmo quadro, com falas e reações cruzadas.
 * Cada batida é uma lista de comandos da API normal, sem nada especial.
 * Serve de modelo para roteiros automáticos: mude os tempos, o elenco e os comandos.
 */
(function (root) {
  'use strict';
  const STH = root.STH;
  STH.FamilyScene = {
    background: 'kitchen',
    duration: 14,
    cast: [
      { name: 'dan', x: 430, direction: 'three-quarter-right', pose: 'explaining' },
      { name: 'mia', x: 800, direction: 'three-quarter-left', pose: 'arms_crossed', expression: 'skeptical' },
      { name: 'leo', x: 1210, direction: 'three-quarter-left', pose: 'using_phone' },
      { name: 'bea', x: 1500, direction: 'three-quarter-left', pose: 'idle', expression: 'curious' },
      { name: 'biscuit', x: 1730, direction: 'left', pose: 'sitting', animation: 'tail_wag' }
    ],
    beats: [
      { t: 0.3, run: c => { c.dan.setExpression('happy').play('talking'); } },
      { t: 2.6, run: c => { c.dan.play('idle'); c.mia.setExpression('worried').setPose('explaining').play('talking'); } },
      { t: 5.0, run: c => { c.mia.play('idle').setPose('thinking').setExpression('thinking'); c.leo.setExpression('shocked').setPose('pointing').setDirection('left'); c.biscuit.setExpression('curious').play('idle'); } },
      { t: 6.6, run: c => { c.bea.setPose('asking_question').setExpression('curious').play('talking'); c.dan.setExpression('worried'); } },
      { t: 8.8, run: c => { c.bea.play('idle').setPose('hugging'); c.biscuit.setPose('standing').play('bark'); c.dan.setPose('hands_on_head').setExpression('shocked'); } },
      { t: 10.6, run: c => { c.biscuit.setPose('hiding').setExpression('guilty').play('idle'); c.mia.setExpression('reassuring').setPose('comforting').setDirection('three-quarter-right'); } },
      { t: 12.4, run: c => { c.dan.setPose('standing').setExpression('happy'); c.leo.setPose('shrugging').setExpression('sarcastic'); c.bea.setExpression('happy'); } }
    ],
    async setup(scene) {
      scene.clear();
      scene.setBackground(this.background);
      const cast = {};
      for (const a of this.cast) cast[a.name] = await scene.add(a.name, a);
      return cast;
    }
  };
})(typeof self !== 'undefined' ? self : this);
