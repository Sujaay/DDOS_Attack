from distutils.core import setup # type: ignore

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="Sujay Kumar",
    author_email="sujaykumar@gmail.com",
    url="https://github.com/Sujaay/DDOS_Attack.git",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)


