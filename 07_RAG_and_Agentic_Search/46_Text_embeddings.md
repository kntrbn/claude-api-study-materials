# 46. Text embeddings

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287759
**Section:** 07 RAG and Agentic Search

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Text embeddings
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                After breaking a document into chunks, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is essentially a search problem - you need to look through all your text chunks and identify the ones that relate to what the user is asking about.

Semantic Search

The most common approach for finding relevant chunks is semantic search. Unlike keyword-based search that looks for exact word matches, semantic search uses text embeddings to understand the meaning and context of both the user's question and each text chunk.

Text Embeddings

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

Here's how the process works:

You feed text into an embedding model
The model outputs a long list of numbers (the embedding)
Each number ranges from -1 to +1
These numbers represent different qualities or features of the input text

Understanding the Numbers

Each number in an embedding is essentially a "score" for some quality of the input text. However, here's the important caveat: we don't know precisely what each number represents.

While it's helpful to imagine that one number might represent "how happy the text is" or "how much the text talks about oceans," these are just conceptual examples. The actual meaning of each dimension is learned by the model during training and isn't directly interpretable by humans.

VoyageAI for Embeddings

Since Anthropic doesn't currently provide embedding generation, the recommended provider is VoyageAI. You'll need to:

Sign up for a separate VoyageAI account
Get an API key (free to get started)
Add the key to your environment variables

In your .env file, add:
VOYAGE_API_KEY="your_key_here"

Implementation

First, install the VoyageAI library:
%pip install voyageai

Then set up the client and create a function to generate embeddings:

from dotenv import load_dotenv
import voyageai

load_dotenv()
client = voyageai.Client()

def generate_embedding(text, model="voyage-3-large", input_type="query"):
    result = client.embed([text], model=model, input_type=input_type)
    return result.embeddings[0]

When you run this function on a text chunk, you'll get back a list of floating-point numbers representing the embedding. The process is quick and straightforward - the real challenge is understanding how to use these embeddings effectively in your RAG pipeline for finding the most relevant content.

The next step is learning how to compare embeddings to determine which chunks are most similar to a user's question, which forms the core of the semantic search process.
                            
                        
                    

                    
                        
                            Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                002_embeddings.ipynb
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                VoyageAI API Key Directions.pdf
                                                (opens in new tab)

---

## 🎬 Transcript (English)

After extracting some number of text chunks out of a source document, the next step inside of our rag pipeline is to wait for a user to submit a question or query or something like that. And whenever that occurs, we need to take a look at all of our different text chunks and find some number that seems to be somehow related to the user's question so that we can add them as context into our prompt. Now, this process of finding some number of text chunks that are related to the user's question, oh, there's a lot of complexity hidden there. But when we really think about it, this truly is a search problem. We want to take the user's question and search through all of our different chunks until we find some related content and then surface those in some way. The most common way of implementing this inside of a rag pipeline is by implementing a system known as semantic search. Semantic search utilizes something called text embeddings to better understand what each chunk of text is all about and somehow find the chunk of text most related to the user's question. Now we're going to spend a decent amount of time now to focus on text embeddings and really understand what they are doing for us. So let's take a look at a couple of diagrams. A text embedding is a numerical representation of the meaning contained in some text. These text embeddings are generated by something called an embedding model. We feed text into an embedding model, such as I'm very happy today, and the embedding model is going to spit out a long list of numbers. That long list of numbers is our actual embedding. The numbers inside the embedding can range from negative 1 up to positive 1. So now the question is, what do these numbers really mean? Each number inside of an embedding represents a score of some quality of the input text. Now, this is where things get a little confusing because I'm showing two conflicting ideas in this diagram. Let me break this down for you and just be super clear. In reality, we do not know what quality each number inside the embedding is actually tied to. So when I label that first number and say, this is a score of how happy the text is, that's not entirely accurate. We simply don't know what that first number truly represents. Nonetheless, it is very helpful to think of these numbers in that way. It is helpful to imagine that the first number might be one score of how happy the text is. And the second is how much the text is talking about fruit, et cetera. Again, these labels are completely made up by me, and we don't actually know what each number represents, but it's extremely helpful to think about embeddings in this way. So that's how you really want to picture each of these numbers. They are kind of like scores of some different qualities of the input text. The last thing you need to understand is how to actually generate these embeddings. Claude does not currently provide embedding generation. Instead, the recommended provider is Voyage AI. This is a separate company, so requires sign up of a separate account and a different API key. However, it is free to get started and super easy to use. Attached to this lecture is a PDF that will walk you through the process of creating an account and getting an API key. Once you have generated the API key, you need to add it into your .env file right next to your existing Anthropic API key. Make sure you assign it to a variable named Voyage underscore API underscore key. So then right there, you put the generated key that you just got. Once you have updated the .EMV file, I would also encourage you to download attached to this lecture a new notebook file called 002 embeddings. At the very top, you'll find a command that you need to run in order to install the Voyage AI SDK. So make sure you run that command to install the library. Lower on down inside this notebook, I've already put together a function for us called generate embedding. This function is going to take in some piece of text and then return an embedding for it, pretty much as simple as it gets. So if I run all the cells inside here and then run the bottom cell, which is currently opening up the report, chunking the report, and then taking the first chunk and passing into generate embedding. If I then run the cell, I'll get back my list of embeddings. As you can see, generating embeddings is rather quick and rather painless. So the real challenge here is not creating embeddings, it's understanding how they actually fit into our overall rag pipeline. So that's going to be the next topic that we investigate.

---

## 🎬 トランスクリプト（日本語）

ソースドキュメントから複数のテキストチャンクを抽出した後 、Ragパイプライン内の次のステップは 、ユーザーが質問やクエリなどを送信するのを待つことです。 そして、それが起こったときはいつでも、私たちは見る必要があります 、すべての異なるテキストチャンクを調べ、いくつかの数字を見つけます 、それがユーザーの質問に何らかの形で関連しているように見えるようにします。 プロンプトにコンテキストとして追加できるようにします。 さて、このプロセスでは、いくつかのテキストを検索します 、ユーザーの質問に関連するチャンクについてです。 そこには多くの複雑さが隠されています。しかし、いつ 、私たちが本当にそれを考えると、これは本当に検索です 問題です。ユーザーの質問を取り込みたいのです。 関連するコンテンツが見つかるまで、すべての異なるチャンクを検索します。 そして、それらを何らかの方法で提示します。 Rag内でこれを実装する最も一般的な方法は 、セマンティック検索として知られるシステムを実装することです。 セマンティック検索は、テキスト埋め込みと呼ばれるものを使用します。 テキストの各チャンクが何であるかをよりよく理解するために 、そしてユーザーの質問に最も関連するテキストチャンクを見つけます。 ユーザーの質問。 さて、私たちはかなりの時間を費やしてテキストに焦点を当てます 、埋め込みを理解し、それが実際に何をしているのかを理解します。 では、いくつかの図を見てみましょう。 テキスト埋め込みは、テキストに含まれる意味の数値表現です。 これらのテキスト埋め込みは 、埋め込みモデルと呼ばれるものによって生成されます。 テキストを埋め込みモデルにフィードします。 例えば、今日はとても幸せです。 埋め込みモデルは長い数字のリストを出力します。 その長い数字のリストが実際の埋め込みです。 埋め込み内の数字は、マイナス1からプラス1の範囲です。 では、質問は次のとおりです。 これらの数字は実際に何を意味するのでしょうか？ 埋め込み内の各数字は、入力テキストのある品質のスコアを表します。 さて、これは少し混乱するところです。 なぜなら、私はこの図で2つの相反する考えを示しているからです。 これを分解して明確にしましょう。 実際には、埋め込み内の各数字が何に結びついているかを知りません。 そのため、最初の数字にラベルを付けて、これがテキストの幸福度のスコアであると言っても、 それは完全に正確ではありません。その最初の数字が実際に何を表すのか、私たちにはわかりません。 それでも、そのようにこれらの数字を考えることは非常に役立ちます。 最初の数字がテキストの幸福度のスコアの1つであると想像することは役立ちます。 そして、2番目はテキストが果物についてどれだけ話しているかということです。 繰り返しますが、これらのラベルは完全に私が作成したものであり、 、各数字が何を表すのか実際にはわかりません。 しかし、埋め込みをこのように考えることは非常に役立ちます。 したがって、それぞれの数字をどのように思い描くべきかということです。 それらは入力テキストのさまざまな品質のスコアのようなものです。 最後に理解する必要があるのは、これらの埋め込みを実際にどのように生成するかです。 Claudeは現在埋め込み生成を提供していません。 代わりに、推奨されるプロバイダーはVoyage AIです。 これは別の会社です。 そのため、別のメールにサインアップする必要があり、別のAPIキーが必要です。 しかし、開始するのは無料であり、非常に使いやすいです。 この講義に添付されているPDFは、アカウントを作成し、 APIキーを取得するプロセスを説明しています。 APIキーを生成したら、それを.envファイルに追加する必要があります。 既存のAnthropic APIキーの隣にあります。 Voyage_API_key という変数に割り当ててください。 そこで、生成されたキーをそこに入れます。 .envファイルを更新したら、講義に添付されている新しいノートブックファイル 、002_embeddingsをダウンロードすることもお勧めします。 一番上には、インストールする必要があるコマンドがあります。 Voyage AI SDKをインストールするためです。 そのため、ライブラリをインストールするためにそのコマンドを実行してください。 このノートブックの下の方に、generate_embeddingという関数を既に用意しました。 この関数はテキストを受け取り、そのための埋め込みを返します。 非常に簡単です。 もしここで全てのセルを実行し、 そして下部のセルを実行すると、それは現在レポートを開き、 レポートをチャンク化し、最初のチャンクを取得し、 それをgenerate_embeddingに渡しています。 そしてセルを実行すると、埋め込みのリストが返されます。 ご覧の通り、埋め込みの生成は非常に迅速で簡単です。 したがって、実際の問題は埋め込みを作成することではなく、 、それらが私たちのRagパイプライン全体にどのように適合するかを理解することです。 それが次に調査するトピックになります。
