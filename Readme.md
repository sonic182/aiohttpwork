
# AiohttpWork

My cookiecutter to start new aiohttp projects. Project structure very simmilar to Ruby on Rails framework.

# Features

* Tested: generated project has tests done with pytest (98% code tested, see [this sample project](https://github.com/sonic182/aiohttp_sample))
* Small: very few lines of code (except by the custom logger)
* Fast: comes with uvloop and cchardet
* Motor: configured with the mongo asyncronus client motor
* Secure: comes with my custom [json validator](https://github.com/sonic182/json_validator) for only allow trusted input in our endpoints.

# Usage

```bash
cookiecutter https://github.com/sonic182/aiohttpwork
```

# Contribute

1. Fork
2. create a branch `feature/your_feature`
3. commit - push - pull request

Thanks :)
