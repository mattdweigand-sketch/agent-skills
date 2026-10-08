'use strict';
// Every handler skips elements a lesson removes.
document.querySelectorAll('button[data-group]').forEach(button => {
  button.addEventListener('click', () => {
    const group = button.dataset.group;
    document.querySelectorAll(`button[data-group="${group}"]`).forEach(other => {
      other.setAttribute('aria-pressed', String(other === button));
    });
    document.querySelectorAll(`[data-panel="${group}"]`).forEach(panel => {
      panel.hidden = panel.id !== button.dataset.target;
    });
  });
});
document.querySelector('#theme')?.addEventListener('click', event => {
  const light = document.documentElement.dataset.theme !== 'light';
  document.documentElement.dataset.theme = light ? 'light' : 'dark';
  event.currentTarget.setAttribute('aria-pressed', String(light));
  event.currentTarget.textContent = light ? 'Use dark theme' : 'Use light theme';
});
document.querySelector('#copy-sources')?.addEventListener('click', async () => {
  const success = document.querySelector('#copy-success');
  const fallback = document.querySelector('#copy-fallback');
  if (success) success.hidden = true;
  if (fallback) fallback.hidden = true;
  const addresses = [...document.querySelectorAll('.source-list a')].map(link => link.href).join('\n');
  try {
    await navigator.clipboard.writeText(addresses);
    if (success) success.hidden = false;
  } catch {
    if (fallback) fallback.hidden = false;
  }
});
