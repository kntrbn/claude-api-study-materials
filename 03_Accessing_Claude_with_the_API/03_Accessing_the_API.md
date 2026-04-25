# 03. Accessing the API

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287726
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Accessing the API
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively. Let's walk through what happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen.

The Five-Step Request Flow

Every interaction with Claude follows a predictable pattern with five distinct phases: request to server, request to Anthropic API, model processing, response to server, and response to client.

Why You Need a Server

You should never make requests to the Anthropic API directly from client-side code. Here's why:

API requests require a secret API key for authentication
Exposing this key in client code creates a serious security vulnerability
Anyone could extract the key and make unauthorized requests

Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

Making API Requests

When your server contacts the Anthropic API, you can use either an official SDK or make plain HTTP requests. Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby.

Every request must include these essential fields:

API Key - Identifies your request to Anthropic
Model - Name of the model to use (like "claude-3-sonnet")
Messages - List containing the user's input text
Max Tokens - Limit for how many tokens Claude can generate

Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four main stages: tokenization, embedding, contextualization, and generation.

Tokenization

Claude first breaks your input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as numerical definitions that capture semantic relationships.

Words often have multiple meanings. For example, "quantum" could refer to:

A discrete unit of physical quantity (physics)
Quantum mechanics or quantum physics concepts
Something extremely small or subatomic
Quantum computing applications

Contextualization

Claude refines each embedding based on surrounding words to determine the most likely meaning in context. This process adjusts the numerical representations to highlight the appropriate definition.

Generation

The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and controlled randomness to create natural, varied responses.

After selecting each word, Claude adds it to the sequence and repeats the entire process for the next word.

When Claude Stops Generating

After each token, Claude checks several conditions to decide whether to continue:

Max tokens reached - Has it hit the limit you specified?
Natural ending - Did it generate an end-of-sequence token?
Stop sequence - Did it encounter a predefined stop phrase?

The API Response

When generation completes, the API sends back a structured response containing:

Message - The generated text
Usage - Count of input and output tokens
Stop Reason - Why generation ended

Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

Key Takeaways

Understanding this flow helps you:

Design secure architectures that protect your API keys
Set appropriate token limits for your use case
Handle different stop reasons in your application logic
Debug issues by understanding where they might occur in the pipeline

Don't worry about memorizing every detail - the goal is familiarizing yourself with the terminology and overall process you'll encounter when working with Claude's API.

---

## 🎬 Transcript (English)

In this module, we are going to examine how we access Claude and use it to generate some text. To help you understand how this works, I'm going to walk you through the full lifecycle of requests to the Anthropic API. We are going to also take a brief look at what is going on behind the scenes inside of Claude. To get started with this walkthrough, we are going to consider a straightforward, standard chatbot app. Let's imagine that you are building a web app and want to show a chat window to a user in the web browser. When the user enters a message and clicks send, their expectation is that some response will just magically appear. Like I said, I want to examine what is going on behind the scenes here to generate this text and display it on the screen. We are going to break this down into five separate steps. which I've outlined at the top of this diagram. And we're going to walk through each step one by one. When a user enters some text and clicks send, that text is going to be sent off to a server that you, the developer, implement. I mentioned this step just to make one thing clear. You should not attempt to access the Anthropic API directly from a web or mobile app. Whenever you make a request to the API, you are required to include a secret API key. And the best way to make sure that this key stays secret is by never including it inside of your client-side app, and only making a request to the API through a server that you implement. On to step two. Once your server has received a request from the client, the server will make a request directly to the Anthropic API. Usually, you'll make this request through one of the SDKs that Anthropic has published. There are official SDK implementations for Python, TypeScript, JavaScript, Go, and Ruby. Now you don't have to use an SDK if you don't want to. You can also make a plain HTTP request if you wish. When you make this request, you are required to pass along several pieces of data. In particular, you need to include an API key, the name of the model you wish to run, a list of messages, which will include the text that your user submitted, and a max tokens value, which limits the length of the text that Claude will generate. Next up is the Anthropic API, which is where our text will actually be generated. This is where we are going to go into a little bit of detail on the text generation process within the language model. This process is complex, so I'm going to give you a simplified high-level overview. We are going to break down the text generation process into four separate stages. In the first stage, the user's input will be broken down into smaller strings. Each of these text chunks are referred to as a token. These tokens can be whole words, or a part of word, or even a space or a symbol. To keep things clear, we are going to assume that each word forms one single token. Each token is then converted into an embedding. An embedding is a long list of numbers, and you could think of these lists as being like a number-based definition of a given word. Now, an interesting aspect of written language is that a single word can have many possible meanings, and it is only the word's position in a sentence and presence of other words around it that narrows the definition down to one particular meaning. For example, quantum is a word that has many different definitions, and when we see this word, we don't really know what it means until we see other words around it. Likewise, each embedding can be thought of as containing all possible meanings of each word. to refine each embedding down to a single precise definition, a process known as contextualization is used. In contextualization, each embedding is adjusted based upon other embeddings around it. This process helps highlight the meaning of each embedding that makes the most sense given its neighbors. The last step is generation, which is where the text actually gets written. By this point, each of the embeddings has absorbed a tremendous amount of information from their neighbors. The final processed embeddings are then passed to an output layer, which produces probabilities for each possible next word. Now, the model doesn't automatically pick the highest probability. Instead, it uses a mix of probability and randomness to select words, which helps create more natural and varied responses. The selected word is then added onto the end of our list of embeddings and the entire process repeats itself all over. After generating each output token, the model will then pause and ask itself several questions to decide if it is done generating text. First, it will count the number of tokens it has generated and see if it is larger than the max tokens parameter that was provided with the input request. This max tokens parameter will limit the total number of tokens that the model will generate. There is also a special end of sequence token that the model can generate. This is not a regular word. It is a special signal that the model uses to indicate that it has reached what it considers to be a natural end to its generation and that it should stop. Once the generation is complete, the API will send response back to your server. The response will contain a message which has the generated text inside it, along with usage and stop reason. The usage is a count of the number of tokens that you fed into the model and the number of tokens that were generated. The stop reason will tell you exactly why the model decided to stop generating text, whether it hits a natural end of sequence token, or maybe it exceeded the allotted number of tokens. Once your server has received this response, it will send the generated text back to your web or mobile app, where you will display it on a screen. So that is the entire flow. Now, we covered many topics in this video. I don't expect you to memorize any of this just yet. The only goal is to start to get you familiar with some common terminology around accessing Claude through the API.

---

## 🎬 トランスクリプト（日本語）

このモジュールでは、Claudeにどのようにアクセスし、 テキストを生成するかを調べます。この仕組みを理解するために、 Anthropic APIへのリクエストのライフサイクル全体を順を追って説明します。 また、Claudeのバックエンドで何が起こっているかを 簡単に見ていきます。このウォークスルーを開始するために、 シンプルで標準的なチャットボットアプリを 検討します。あなたがウェブアプリを作成していて、 ウェブブラウザでユーザーにチャットウィンドウを表示したいとしましょう。 ユーザーがメッセージを入力して送信をクリックすると、 何らかの応答が魔法のように表示されることが 期待されます。先ほど言ったように、このテキストを生成し、 画面に表示するためにバックエンドで何が起こっているかを 調べたいと思います。これを5つの個別のステップに分解します。 これはこの図の上部に概要を示したものです。各ステップを一つずつ見ていきます。 ユーザーがテキストを入力して送信をクリックすると、そのテキストは 開発者であるあなたが実装するサーバーに送信されます。 このステップは、一つのことを明確にするために言及しました。 Anthropic APIには、ウェブアプリやモバイルアプリから 直接アクセスしようとしないでください。APIにリクエストを行う際には 常に、秘密のAPIキーを含める必要があります。 そして、このキーを秘密にしておく最良の方法は、 クライアントサイドアプリの中に決して含めず、 あなたが実装したサーバーを通してのみAPIにリクエストを行うことです。 ステップ2に移りましょう。サーバーがクライアントからの リクエストを受け取ると、サーバーはAnthropic APIに直接 リクエストを行います。通常、Anthropicが公開している SDKのいずれかを通してこのリクエストを行います。 公式のSDK実装は、Python、TypeScript、JavaScript、 Go、Ruby向けにあります。SDKを使いたくない場合は 使用する必要はありません。必要であれば、プレーンなHTTPリクエストも可能です。 このリクエストを行う際には、いくつかのデータを含める必要があります。 特に、APIキー、実行したいモデルの名前、 ユーザーが送信したテキストを含むメッセージのリスト、 そしてClaudeが生成するテキストの長さを制限するmax_tokens値が必要です。 次はAnthropic APIです。ここで実際にテキストが生成されます。 ここでは、言語モデル内のテキスト生成プロセスについて少し詳しく説明します。 このプロセスは複雑なので、簡略化されたハイレベルな概要を説明します。 テキスト生成プロセスを4つの個別のステージに分解します。 最初のステージでは、ユーザーの入力がより小さな文字列に分割されます。 これらのテキストの断片はそれぞれトークンと呼ばれます。 これらのトークンは、単語全体、単語の一部、スペース、記号でも構いません。 分かりやすくするために、各単語が1つのトークンを形成すると仮定します。 各トークンは、次に埋め込みに変換されます。埋め込みは数字の長いリストであり、 これらのリストを単語の数値ベースの定義のようなものだと考えることができます。 書かれた言語の興味深い側面は、単一の単語が多くの可能な意味を持つことがあり、 その単語の意味を特定の一つに絞り込むのは、その単語の文中の位置と 周りの他の単語の存在だけです。例えば、クォンタムは 多くの異なる定義を持つ単語であり、この単語を見たとき、 周りの他の単語を見るまでその意味はよく分かりません。同様に、 各埋め込みは、単語のすべての可能な意味を含んでいると考えることができます。 各埋め込みを単一の正確な定義に絞り込むために、 文脈化と呼ばれるプロセスが使用されます。 文脈化では、各埋め込みは周りの他の埋め込みに基づいて調整されます。 このプロセスは、隣接するものを考慮して最も意味のある埋め込みの意味を 強調するのに役立ちます。最後のステップは生成です。 ここでテキストが実際に書き込まれます。この時点までに、 各埋め込みは、その隣接要素から大量の情報を吸収しています。 最終的に処理された埋め込みは、出力層に渡され、 可能な次の単語ごとの確率を生成します。 モデルは自動的に最も高い確率を選択するわけではありません。 代わりに、確率とランダム性を組み合わせて単語を選択し、 より自然で多様な応答を作成するのに役立ちます。 選択された単語は、埋め込みリストの末尾に追加され、 プロセス全体が繰り返されます。 各出力トークンを生成した後、モデルは一時停止し、 テキストの生成を終了したかどうかを判断するために、 いくつかの質問をします。まず、生成したトークンの数を確認し、 入力リクエストで提供されたmax_tokensパラメータよりも大きいかどうかを確認します。 このmax_tokensパラメータは、モデルが生成する総トークン数を制限します。 また、モデルが生成できる特別なシーケンス終了トークンもあります。 これは通常の単語ではなく、モデルが生成の自然な終了と 判断し、停止すべきであることを示すための特別な信号です。 生成が完了すると、APIは応答をサーバーに返送します。 応答には、生成されたテキストが含まれるメッセージと、 使用状況と停止理由が含まれます。 使用状況は、モデルに入力したトークンの数と、 生成されたトークンの数を示します。 停止理由は、モデルがテキスト生成を停止した理由を正確に示します。 自然なシーケンス終了トークンに達したのか、 それとも割り当てられたトークン数を超えたのかです。 サーバーがこの応答を受け取ると、生成されたテキストを ウェブアプリまたはモバイルアプリに送信し、そこで画面に表示します。 これが全体のフローです。このビデオでは多くのトピックを扱いましたが、 現時点では何も暗記する必要はありません。 唯一の目標は、API経由でClaudeにアクセスする際の一般的な専門用語に 慣れていただくことです。
