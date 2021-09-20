import logging

logger = logging.getLogger()
handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)


# common methods


def read(file_name: str) -> str:
    with open(file_name, 'r') as file:
        return file.read()


#  first word will be replaced by second one
data_to_replace = [
    ('full-stack', 'fullstack'),
    ('full-stack', 'fullstack'),
    ('full-time', 'fulltime'),
    ('back-end', 'backend'),
    ('back end', 'backend'),
    ('front-end', 'frontend'),
    ('dev-ops', 'devops'),
    ('team-lead', 'teamlead'),
    ('tech-lead', 'techlead'),
    ('science', 'scientist'),
    ('data-scientist', 'datascientist'),
    ('qa-engineer', 'qa'),
    ('automation engineer', 'qa'),
    ('quality-assurance', 'qa'),
    ('-js-', '-javascript-'),
    ('sr-', 'senior-'),
    ('mid-', 'middle-'),
    ('ruby-on-rails', 'rubyonrails'),
    ('site-reliability-engineer', 'sre'),
    ('reactjs', 'react'),
    ('golang', 'go'),
    ('big-data', 'bigdata'),
    # for Tags
    ('postgres\n', 'postgresql\n'),
    ('quality assurance', 'qa'),
    ('full stack', 'fullstack'),
    ('full-stack', 'fullstack'),
    ('dev ops', 'devops'),
    ('qa engineer', 'qa'),
    ('react.js', 'react'),
    ('front-end', 'frontend'),
    ('data scientist', 'data science'),
    ('nodejs\n', 'node\n'),
    ('node.js\n', 'node\n'),
    ('fullstack development\n', 'fullstack developer\n'),
    ('java ee', 'java'),
    ('java-11', 'java'),
    ('java-ee', 'java'),
    ('spring-mvc', 'spring'),
    ('spring-boot', 'spring'),
    ('ios developer', 'ios'),
    ('ios sdk', 'ios'),
    ('android developer', 'android'),
    ('android sdk', 'android'),
    ('android ndk', 'android'),
    ('amazon-web-services', 'aws'),
    ('c#', '.net'),
    ('.net (core)', '.net'),
    ('vue.js', 'vue'),
    ('vuejs', 'vue'),
    ('azure cloud', 'azure'),
    ('html5', 'html'),
    # ('django', 'python'),
]
