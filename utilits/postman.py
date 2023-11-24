from telegraph import Telegraph


class Postman:
    def __init__(self, token = None, bot_photo = '/file/c7038df96498dca8c07d6.png'):
        self.token = token
        self.bot_photo = bot_photo
        self.telegraph = Telegraph(access_token = token)
    
    def upload(self, data : dict, path = "Kop-Soraladigan-Savollar-11-24", title = "Ko'p So'raladigan Savollar", autor = "Grand Nasiya Bot"):
        html_content = f"<img src='{self.bot_photo}' alt='Uploaded Photo'>"
        n = 1
        for question, answer in data.items():
            html_content += f"<h4>{n}. {question}</h4>"
            html_content += f"<p><em>{answer}</em></p>"

            self.telegraph.edit_page(html_content = html_content, title = title, path = path, author_name = autor)

            n+=1
        
        return True


if __name__ == '__main__':
    postman = Postman(token = 'none')
    data = {f"savol {n}" : 'javob' for n in range(10)}
    print(data)
    postman.upload(data=data)
