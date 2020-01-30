from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(
    globals(), "lino_mercato",
    languages="en de fr".split(),
    # tolerate_sphinx_warnings = True,
    blogref_url='http://luc.lino-framework.org',
    revision_control_system='git',
    locale_dir='lino_mercato/lib/mercato/locale',
    cleanable_files=['docs/api/lino_mercato.*'],
    demo_projects=[
        'lino_mercato.projects.demoTrading'])
