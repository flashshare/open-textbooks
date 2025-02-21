import os
from urllib.parse import quote
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.directives.patches import Figure

from utils import parse_options, generate_style, ReviewStatus


#DEFAULT_BASE_URL = 'https://openla.ewi.tudelft.nl/applet/'
DEFAULT_BASE_URL = ''

class AppletDirective(Figure):
	option_spec = Figure.option_spec.copy()
	option_spec.update({
		'url': directives.unchanged_required,
		'fig': directives.unchanged_required,
		'title': directives.unchanged,
		'background': directives.unchanged,
		'autoPlay': directives.unchanged,
		'position': directives.unchanged,
		'isPerspectiveCamera': directives.unchanged,
		'enablePan': directives.unchanged,
		'distance': directives.unchanged,
		'zoom': directives.unchanged,
		'height': directives.unchanged,
		'width': directives.unchanged,
		'status': directives.unchanged
	})
	required_arguments = 0


	def run(self):
		url = self.options.get('url')
		fig = self.options.get('fig')
		assert url is not None
		assert fig is not None

		self.arguments = [fig]
		self.options['class'] = ['applet-print-figure']
		(figure_node,) = Figure.run(self)

		# Generate GET params and inline styling
		params_dict = parse_options(self.options)
		params = '&'.join([f'{key}={quote(value)}' for key, value in params_dict.items()])
		status = ReviewStatus.parse(self.options.get('status', ''))
		style = generate_style(self.options.get('width', None), self.options.get('height', None), status)

		base_url = os.environ.get('BASE_URL', DEFAULT_BASE_URL)
		full_url = f'{base_url}{url}{"?" if params else ""}{params}'
		applet_html = f'''
			<div class="applet" style="{style}">
				<noscript class="loading-lazy">
					<iframe src="{full_url}" allow="fullscreen" loading="lazy" frameborder="0"></iframe>
				</noscript>
			</div>
		'''
		applet_node = nodes.raw(None, applet_html, format='html')

		# Add applet as the first child node of figure
		figure_node.insert(0, applet_node)

		return [figure_node]


def setup(app):
	app.add_directive('applet', AppletDirective)
	return {
		'version': '0.1',
		'parallel_read_safe': True,
        'parallel_write_safe': True,
	}
