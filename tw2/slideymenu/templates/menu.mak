<div id='${w.attrs['id']}-button'>${w.label}</div>
<div id='${w.attrs['id']}-menu'>
% for entry in w.items:
	<h3>
% if 'href' in entry:
	<a href="${entry['href']}">${entry['label']}</a>
% else:
	${entry['label']}
% endif
	</h3>
% endfor
</div>
<script type="text/javascript">
setupSlideyMenu('${w.selector}', ${w._options});
</script>
