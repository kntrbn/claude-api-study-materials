# 05. Making a request

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287725
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Making a request
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Making your first request to the Anthropic API is straightforward once you understand the basic setup and structure. This guide walks through the essential steps to get Claude responding to your prompts using Python.
Setting Up Your Environment
Before making any API calls, you need to install the required packages and configure your API key securely.
First, install the necessary dependencies in your Jupyter notebook:
%pip install anthropic python-dotenv
Next, create a .env file in the same directory as your notebook to store your API key securely:
ANTHROPIC_API_KEY="your-api-key-here"
This approach keeps your API key out of your code and prevents accidentally committing it to version control. Always add .env to your .gitignore file.
Load the environment variables and create your API client:
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
The Create Function
The core of making API requests is the client.messages.create() function. This function requires three key parameters:

model - The name of the Claude model you want to use
max_tokens - A safety limit on response length (not a target)
messages - The conversation history you're sending to Claude

The max_tokens parameter acts as a safety mechanism. If you set it to 1000, Claude will stop generating after 1000 tokens even if it has more to say. Claude doesn't try to reach this limit - it just writes what it thinks is appropriate and stops if it hits the maximum.
Understanding Messages
Messages represent the conversation between you and Claude, similar to a chat application. There are two types of messages:

User messages - Content you want to send to Claude (written by humans)
Assistant messages - Responses that Claude has generated

Each message is a dictionary with a role (either "user" or "assistant") and content (the actual text).
Making Your First Request
Here's a complete example of making a request to Claude:
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
When you run this code, Claude will process your request and return a response object containing the generated text along with metadata about the request.
Extracting the Response
The response object contains a lot of information, but you usually just want the generated text. Access it using:
message.content[0].text
This gives you clean, readable output like: "Quantum computing is a type of computation that leverages quantum mechanics principles like superposition and entanglement to process information using quantum bits (qubits), potentially solving certain complex problems exponentially faster than classical computers."
With these basics in place, you can start experimenting with different prompts and building more complex interactions with Claude.

---

## 🎬 Transcript (English)

We have done quite a bit of talking, so in this video, we're going to change things and get our hands dirty by writing out a little bit of code. We're going to learn how to make a simple and basic request off to the Anthropic API. I'm going to walk you through four setup steps. So step one, we're going to open up a Jupyter notebook and install the Anthropic Python SDK, along with a package called python-dotenv. To get started, I'm going to open up a notebook on my own. I've already added in some comments to my notebook just to guide myself through this process. In step one up here, I'm going to add in a magic install command, so percent, pip, install, anthropic, python-dotenv. If you're writing your notebook inside of Visual Studio Code as I am, you might notice a red syntax error coming from the percent over here. If you see that syntax error, it is totally fine. You can ignore it. Once I've written out this command, I'm going to run it to install these packages. I'm then going to clear the output just so you can see what's going on my screen a little bit more easily. Next, we are going to use that python-dotenv package to store and load our API key. As a reminder, I put in some directions on creating API key in the previous lecture. So if you did not create an API key, I would encourage you to go back to the previous lecture and find those directions. To store this key inside of my editor, I'm going to create a file in the same directory as my notebook with a very special name. I'm going to name this file.env. And then inside of here, I'm going to place the API key that I generated a moment ago. I will write out exactly ANTHROPIC_API_KEY, and then an equal sign. And then inside of double quotes, I will put in that key. As a quick side note, the whole reason that we are creating this file and putting our key inside of here is so that we can now ignore this file when we are making use of version control. So that we do not accidentally commit this file, say, to git, and then accidentally push it up to some public repository where anyone can see this file. So again, if you're making use of Git or a similar version control system, I would encourage you to make sure that you ignore this file any time you are committing your work. Now, back inside of my notebook, I can securely load up that environment variable. Then, onto step number three, where we will create our API client using the Anthropic package. Inside the cell, I'm also going to declare a variable name model. This will be a string. It's going to contain the name of the model that we want to run inside of the Anthropic API. We are going to use Claude 3.7 Sonnet. Now onto the last step, where we are going to actually make a request using that client that we just created. Before we write out any code, however, I want to show you a little bit of terminology, just some stuff that's going to make things a little bit easier down the line. So the first thing to understand here is that we are going to access Claude by using the create function inside the Anthropic SDK. This function requires three different keyword arguments, a model, max tokens, and messages. The model keyword argument is just going to be the name of the model we want to run. We already defined that variable ahead of time in our previous cell. The second required keyword argument is max_tokens. This sets a maximum budget on a number of tokens that Claude can generate. For example, if we pass in a max tokens of 1000, if Claude tries to generate anything longer than that, then the generation will be automatically stopped, and we will receive back the first 1000 tokens that were generated. One thing to note here is that Claude doesn't try to target your number of max_tokens. In other words, Claude won't try to write a response of 1000 tokens, it'll just write whatever response it thinks is appropriate. And as such, you should really view max_tokens as being like a safety mechanism to ensure that you're not generating too much text. Finally, messages. And this is the part that I really want to focus on because messages are going to be a huge focus for us in the coming videos. To understand what messages are all about, I would like you to think back to the chat application we discussed a moment ago. So a user might type in some question to Claude and then expect to get an answer back. The messages that we're talking about when we pass these things into this create function are meant to represent exchanges like this. There are two types of messages, a user message and assistant message. User messages contain text that we want to feed into Claude. The content inside of a user message is text that either a user or you and I as developers have authored. In other words, a user message will contain text that has been written by some person. The second type of message is an assistant message. These messages contain text that have been produced by a model and sent back to us. Now, at this point, I think we have enough knowledge to at least make our first request. So let's do that and then discuss messages a little bit more. Back inside of my notebook, in the very last cell, I'm going to declare a variable of message that will come from client.messages.create And I'm going to pass in those different arguments that we just discussed. So I'll put in a model of model, a max_tokens, and I'll use 1000 here, which I think is definitely a safe limit, and then a list of input messages. So inside here, I'm going to put in one single user message, and it will contain my question or my query that I want to send off to Claude. To create a user message, we'll create a dictionary that will have a role of user, and then a content that will contain the actual string that we want to send into Claude. So in this case, I'm going to ask Claude to define quantum computing with something like what is quantum computing answer in one sentence. Then I'm going to run this and we'll take a moment or two to run because we are actually accessing Claude here. And then in the next cell down, I'm going to try to print out the message variable. We'll see what we get. All right, so inside of here, we can see that there's a lot of stuff coming out, but noticeably, we have a definition right around here of what quantum computing actually is. So inside of this message variable that we got back, our text is kind of deeply nested. We very often want to get just the text that Claude has generated, and very often we don't really care about any of these other properties that are contained inside this thing. So to access just the generated text, we would write out message.content[0].text like so. And if I run that cell again, now I'll see just the generated text and nothing else.

---

## 🎬 トランスクリプト（日本語）

かなりの時間お話ししたので、この動画では少し 変えて、実際にコードを書いてみましょう。簡単な 基本的なリクエストをAnthropic APIに送信する方法を学びます。 4つのセットアップ手順を説明します。ステップ1は、 Jupyter Notebookを開いて、Anthropic Python SDKとpython-dotenvというパッケージをインストールします。 開始するために、自分でNotebookを開きます。すでに Notebookにいくつかのコメントを追加して、自分自身を ガイドするようにしています。ここのステップ1では、 マジックインストールコマンドを追加します。つまり、パーセント、 pip、インストール、anthropic、python-dotenvです。 私がやっているようにVisual Studio CodeでNotebookを書いている場合、 パーセントから赤い構文エラーが表示されるのに気づくかもしれません。 もしその構文エラーが見られたら、 それは全く問題ありません。無視できます。 このコマンドを書き終えたら、実行してこれらのパッケージをインストールします。 その後、出力をクリアします。そうすれば、画面で何が起こっているかを もう少し簡単に見ることができます。次に、 そのpython-dotenvパッケージを使用してAPIキーを 保存して読み込みます。念のため、 前の講義でAPIキーを作成する手順を入れました。 ですから、APIキーを作成しなかった場合は、 前の講義に戻って、それらの手順を見つけることをお勧めします。 このキーをエディタ内に保存するために、 Notebookと同じディレクトリに、非常に特別な名前のファイルを作成します。 このファイルの名前を.envとします。そして、その中に、 先ほど生成したAPIキーを配置します。 ANTHROPIC_API_KEYと書き、 次に等号を置きます。そして二重引用符の中に、 そのキーを入れます。ちょっとした余談ですが、 このファイルを作成してキーを保存する理由は、 バージョン管理を使用する際に、このファイルを無視できるようにするためです。 例えばGitにこのファイルをコミットしてしまい、 誤って公開リポジトリにプッシュして、誰でもこのファイルを見られるようにしないためです。 したがって、繰り返しになりますが、Gitや類似のバージョン管理システムを使用している場合は、 作業をコミットする際は、常にこのファイルを無視するようにしてください。 さて、Notebookに戻って、その環境変数を安全に読み込むことができます。 次にステップ3に移ります。そこでは、Anthropicパッケージを使用してAPIクライアントを作成します。 このセル内でも、モデルという変数名を宣言します。 これは文字列で、Anthropic API内で実行したいモデルの名前が含まれます。 Claude 3.7 Sonnetを使用します。 それでは最後のステップに進みます。そこで、先ほど作成したクライアントを使用して実際にリクエストを行います。 しかし、コードを書く前に、少し専門用語を紹介します。 これは後で物事を簡単に理解するために役立つでしょう。 まず理解すべきことは、Anthropic SDKのcreate関数を使用してClaudeにアクセスすることです。 この関数は3つの異なるキーワード引数を必要とします。 モデル、最大トークン、メッセージです。 モデルキーワード引数は、実行したいモデルの名前です。 すでに前のセルでその変数を定義しました。 2番目の必須キーワード引数はmax_tokensです。 これはClaudeが生成できるトークン数に最大予算を設定します。 例えば、max_tokensに1000を渡した場合、 Claudeがそれよりも長いものを生成しようとすると、 生成は自動的に停止され、生成された最初の1000トークンが返されます。 ここで注意すべき点は、Claudeはmax_tokensの数を目標としないということです。 つまり、Claudeは1000トークンの応答を書こうとはせず、 適切なと思う応答を書くだけです。 したがって、max_tokensは、テキストが生成されすぎるのを防ぐための安全メカニズムと 考えるべきです。最後に、メッセージです。 そして、これが私が本当に焦点を当てたい部分です。 なぜなら、メッセージは今後の動画で非常に重要な焦点となるからです。 メッセージについて理解するために、先ほど説明したチャットアプリケーションを 思い出してほしいと思います。ユーザーがClaudeに何か質問を入力し、 それに対する回答を期待するかもしれません。 これらのものをcreate関数に渡す際に話しているメッセージは、 このようなやり取りを表すものです。 メッセージには2つのタイプがあります。 ユーザーメッセージとアシスタントメッセージです。 ユーザーメッセージには、Claudeに渡したいテキストが含まれます。 ユーザーメッセージの内容は、ユーザーまたは開発者である私たちによって作成された テキストです。つまり、ユーザーメッセージには誰かによって書かれたテキストが含まれます。 2番目のタイプのメッセージはアシスタントメッセージです。 これらのメッセージには、モデルによって生成され、私たちに返されたテキストが含まれます。 さて、この時点で、最初の要求を行うのに十分な知識があると思います。 では、それを実行してから、メッセージについてもう少し詳しく説明しましょう。 Notebookに戻って、最後のセルに、 client.messages.createから取得するメッセージという変数を宣言します。 そして、先ほど説明した異なる引数を渡します。 モデルはmodel、max_tokensは1000を使用します。 これは安全な制限だと思います。 そして、入力メッセージのリストを渡します。 ここには、単一のユーザーメッセージを1つ入れます。 それは私の質問やClaudeに送信したいクエリを含みます。 ユーザーメッセージを作成するには、 ロールがuser、コンテンツがClaudeに送信したい実際の文字列を含む辞書を作成します。 したがって、この場合は、Claudeに量子コンピューティングを定義するように依頼します。 量子コンピューティングとは何ですか？一文で答えてください。 それからこれを実行すると、少し時間がかかります。 なぜなら、実際にClaudeにアクセスしているからです。 そして、その下の次のセルで、メッセージ変数を表示しようとします。 何が得られるか見てみましょう。 さて、ここを見ると、多くのものが出力されていますが、注目すべきは、 量子コンピューティングが実際に何であるかの定義がここにあることです。 私たちが受け取ったこのメッセージ変数内では、 私たちのテキストは少し深くネストされています。 私たちはClaudeが生成したテキストだけを取得したいことがよくあり、 そして、この中にある他のプロパティにはあまり関心がありません。 生成されたテキストにアクセスするには、 message.content[0].textのように記述します。 そして、そのセルを再度実行すると、生成されたテキストだけが表示され、 他のものは何も表示されなくなります。
