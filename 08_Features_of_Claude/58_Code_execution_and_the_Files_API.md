# 58. Code execution and the Files API

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287777
**Section:** 08 Features of Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Code execution and the Files API
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                The Anthropic API offers two powerful features that work exceptionally well together: the Files API and Code Execution. While they might seem separate at first, combining them opens up some really interesting possibilities for delegating complex tasks to Claude.

Files API

The Files API provides an alternative way to handle file uploads. Instead of encoding images or PDFs directly in your messages as base64 data, you can upload files ahead of time and reference them later.

Here's how it works:

Upload your file (image, PDF, text, etc.) to Claude using a separate API call
Receive a file metadata object containing a unique file ID
Reference that file ID in future messages instead of including raw file data

This approach is particularly useful when you want to reference the same file multiple times or when working with larger files that would be cumbersome to include in every request.

Code Execution Tool

Code execution is a server-based tool that doesn't require you to provide an implementation. You simply include a predefined tool schema in your request, and Claude can optionally execute Python code in an isolated Docker container.

Key characteristics of the code execution environment:

Runs in an isolated Docker container
No network access (can't make external API calls)
Claude can execute code multiple times during a single conversation
Results are captured and interpreted by Claude for the final response

Combining Files API and Code Execution

The real power comes from using these features together. Since the Docker containers have no network access, the Files API becomes the primary way to get data in and out of the execution environment.

Here's a typical workflow:

Upload your data file (like a CSV) using the Files API
Include a container upload block in your message with the file ID
Ask Claude to analyze the data
Claude writes and executes code to process your file
Claude can generate outputs (like plots) that you can download

Practical Example

Let's look at a real example using streaming service data. The CSV file contains user information including subscription tiers, viewing habits, and whether they've churned (canceled their subscription).

First, upload the file using a helper function:

file_metadata = upload('streaming.csv')

Then create a message that includes both the uploaded file and a request for analysis:

messages = []
add_user_message(
    messages,
    [
        {
            "type": "text",
            "text": """Run a detailed analysis to determine major drivers of churn.
            Your final output should include at least one detailed plot summarizing your findings."""
        },
        {"type": "container_upload", "file_id": file_metadata.id},
    ],
)

chat(
    messages,
    tools=[{"type": "code_execution_20250522", "name": "code_execution"}]
)

Understanding the Response

When Claude uses code execution, the response contains multiple types of blocks:

Text blocks - Claude's analysis and explanations
Server tool use blocks - The actual code Claude decided to run
Code execution tool result blocks - Output from running the code

Claude might execute code multiple times during a single response, iteratively building up its analysis. Each execution cycle includes the code and its results.

Downloading Generated Files

One of the most powerful features is Claude's ability to generate files (like plots or reports) and make them available for download. When Claude creates a visualization, it gets stored in the container and you can download it using the Files API.

Look for blocks with type: "code_execution_output" in the response - these contain file IDs for generated content:

download_file("file_id_from_response")

The result is a comprehensive analysis with professional visualizations that

---

## 🎬 Transcript (English)

In this video, we're going to take a look at two features offered through the Anthropic API. And these two features are going to seem a little bit different, just a little bit separate, but it turns out they can be combined together in really interesting ways. So let's get to it. We're going to first begin by understanding what the files API is all about. Earlier on inside this course, we discussed how you can pass images into Claude and ask Claude to interpret the image itself. And I showed you how we can include an image block, which can include the actual raw image data, and coded in base64. We also saw a very similar process being used for uploading of PDF documents as well. The file's API allows for a little bit of a twist on this whole system. With a file API, we can make an individual request ahead of time to upload a particular document, be it a PDF or an image or a text file or whatever else. So we might make an initial request off to Claude to upload that file. We'll then get back something called a file metadata object. This file metadata object contains some different information, but the most interesting or important property to us is the file ID. This ID allows us to refer back to that uploaded file at some point in time in the future. So then later on, at some point in the future, a user can submit a message like what do you see inside this image. And inside of our image block right here, rather than including the raw file data from the image itself, we can include just the file ID. So we can put in the file ID right there. And that's going to get Claude to go and find that image that we had uploaded ahead of time. Claude is then going to try to interpret the image as best as it can. So the file API allows us to upload a file ahead of time and then make a request later on and include some data about the original file inside the request to Claude. So you can really just think of this as being another way that we can provide an image or PDF to Claude. Now that we understand the basics behind this file API, just the idea that allows us to submit a file and then refer back to it at a future point in time, we are going to switch gears and discuss the other focus of this video, which is code execution. Code execution is a server-based tool. So we do not have to provide an actual implementation for this tool. All we have to do is provide a predefined tool schema. Inside of a initial request we make off to Claude, we will include this especially defined tool schema, along with whatever user-submitted message we want to include. Then behind the scenes, Claude can optionally decide to execute some amount of Python code inside of an isolated Docker container. Claude can run code inside this container multiple different times. Whatever Claude prints up from these code executions will be sent back to Claude and the Claude can interpret the results and write a final response to us. These Docker containers do not have any network access. That means that Claude cannot write out any code that will make a network request or attempt to access any kind of outside API. Instead, to get information into the Docker container and to get information out of it, we rely upon mixing together that file API that we just discussed, along with this code execution tool. So let me show you how this works in total. Let's imagine that we have a CSV file called maybemydata.csv, and it contains a lot of tabular information that we want to get analyzed by Claude. Rather than going through some really complicated code setup where we ask Claude to write out some code and then we manually execute that ourselves, we can instead make use of this file API and the code execution tool together to get Claude to automatically analyze the file and produce some results for us. So to do so, we will first use the file API to upload our CSV file. So we'll initially up here, upload our CSV file with some amount of data inside of it. And that's going to give us back a file ID. We will then include that file ID inside of a follow-up request to Claude. So we will add in something called a container upload block. A container upload block just means that we want to take a file that we previously uploaded to Claude and somehow inject it or place it inside of the container. So we're going to add in this very specially crafted block with a type of container upload and a file ID property of whatever ID we got back from when we had uploaded our original file. Then inside of a separate text block, we'll ask Claude to do some analysis, maybe something as simple as analyze the data inside this file. Then behind the scenes, Claude is going to make use of the code execution tool. Claude is going to have access to that uploaded file inside the Docker container. So Claude can write out some code to analyze the file, process the results, and then give us a full report of all the data inside that file. Let's now take a look at an example of this entire flow. So I've put together a notebook at a time called 005 code execution. I've also created a separate CSV file called streaming.csv. Inside of here is a bunch of fake data from a video streaming service. This file contains information about particular users, what subscription tier they are included in, so what level of access they have, and then a lot of statistics about this particular user. So in total number of hours they have viewed, top genre, et cetera, et cetera, and then at the very end, the very last column is called churned. Churned is an indication of whether or not the user has canceled their subscription. So as euro means they have not canceled their subscription, and one means they have canceled their subscription. Now I could write out a lot of code to analyze the data inside this file and figure out whether or not there is some correlation between these different features and whether or not a user has canceled their subscription. But instead of doing all this myself, I might decide to just hand the entire task off to Claude. I could first upload this stringing.csv file and then ask Claude to make use of its code execution tool to do an analysis of all the data inside of here. So let me show you how we would do that. First, back inside the notebook, I want you to take a look at the helper function cell. If you scroll down a little bit, you'll notice that I added in a couple of different functions. I added in a upload function, which will automatically upload a particular file given a file path. I have added in a list files function, which will list out all the different files we have uploaded to Claude. We can delete a file, we can download a file, and we get information about a particular file as well. We're going to make use of these functions very shortly. So I'm going to collapse that cell, and of course, make sure that I run it as well. Then in the next cell down, I'm going to attempt to upload the streaming.csv file. So I'm going to run that cell right away. And we'll get back our file metadata object. And inside of here, there's our ID. So that is the unique ID that identifies this file to Claude. And if we ever want to include it inside of a conversation in the future, we're referred to that particular ID. Then inside the next cell down, I've got a short prompt that is asking Claude to run a detailed analysis and figure out why customers are canceling their subscription. I'm also asking Claude to print out a plot that summarizes all of its findings. Then after that, I've got the Container Upload block, which is going to actually include that uploaded file inside of our request. So now I want to run the cell and just be aware that whenever you make use of code execution, it sometimes actually takes a little bit of time to complete. The response we get back is going to contain a tremendous amount of text. Inside this message is going to be all the code that Claude decided to write, along with all the print statements and output that it got, along with some final analysis as well. Claude can decide to run code multiple times inside the container, so we might actually see multiple code blocks and multiple execution results inside this message. Now to help you understand what's going on inside the message, I took all that content and I format it just a little bit more nicely so we can understand what's happening. So here's that message. I got my content list with a variety of different blocks inside of it. The first block is a text block, which is going to contain some amount of text that just has Claude framing the initial problem. Claude is then going to provide a server tool use block. This is going to contain some amount of code that Claude wants to run inside the container. And then here is our code execution tool result. It's going to contain some information about the actual execution of that code. So data from standard out, standard error, return code in case there's any error handling required, and so on. And then it looks like in this case, Claude decided to run some more code after that. So it did some further analysis right here, got back some more results, and it did some more analysis, and so on. So in this case, Claude ran some code several times in row to do some thorough analysis. Now, whether or not you decide to show all this content to your users is totally up to you and the particular application that you are working on. If you want to, you could build up a really nice looking report, maybe something like this. So I took all that information that we were just looking at, and I used Claude to just format it very nicely. So now I can see the initial response right there. So that's the exact information from the initial text block that we got back. Then here's my code execution tool. There's the code that Claude decided to run, along with the output from executing it. And we could see this is repeated several times in a row. So now I've got some more text right here, another code execution, and so on. Finally, I want to show you one of the most interesting aspects of code execution. So you may recall that back inside this prompt that I sent off, I asked Claude to include one detailed plot summarizing its findings. Claude behind the scenes did generate a plot inside of a image file, and that is stored inside of our Docker container. We can use the file API to download that generated plot inside of the Docker container. Let me show you how. First, I'm going to go and take a close look at the message that I formatted over here. So if I scroll through, I might eventually see a text block that has an extra nested content property. And inside that, I might see a type of code execution output. So here's mine right here. If you don't see it inside of your response, try searching for code execution output. Right underneath that is a file ID. So I can use this file ID to download the file. I'm going to copy it, go back over to my notebook, I'm going to go down to the very bottom and add in a new cell. Here we go. I'm going to call download file, which was one of those predefined functions that we took a look at at the start of this video. And I'm going to paste in the file ID that I just found inside the response. I'm going to run this. It's going to run successfully. And now if I take a look at the same directory that my notebook is in, I'm going to find maybe a PNG or a JPEG file inside there. Their name is going to be random. It's not truly random per se. It's going to be whatever Claude decided to name it. If I then open up that file, if I then open up that file, I'll see a bunch of information that Claude extracted from that CSV file. So this is a great visualization that tells me everything I need to know. So churn right by viewing hours, by monthly cost ranges, and so on, Claude did a very thorough analysis here to help me understand the contents of this file. So as you can see, based upon this demo, combining together the file API and the code execution tool allows us to delegate rather complex tasks off to Claude. Of course, you are not limited to just doing data analysis. You can use the combination of code execution along with the files API to execute a wide variety of different tasks. And it's really up to you to decide how to integrate this into your application.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、Anthropic API を通じて提供される 2 つの機能を見ていきます。この 2 つの機能は 少しずつ異なり、少しばかり別々に見えるかもしれませんが、 非常に興味深い方法で組み合わせることができることが判明しました。 それでは始めましょう。まず、ファイル API が 何であるかを理解することから始めます。以前 このコースで、Claude に画像を渡して、 Claude に画像を解釈させる方法を説明しました。 画像ブロックを含める方法を示しました。 画像ブロックには実際の生画像データを含めることができ、 Base64 でエンコードされます。また、 PDF ドキュメントのアップロードにも 非常に似たプロセスが使用されているのを見ました。ファイル API は このシステム全体に少しひねりを加えてくれます。 ファイル API を使用すると、個別の リクエストを事前に行い、特定のドキュメントを アップロードできます。PDF、画像、テキストファイルなど、 何でも構いません。したがって、最初に Claude に ファイルをアップロードするリクエストを送信し、次に ファイルメタデータオブジェクトと呼ばれるものを取得します。このファイルメタデータ オブジェクトにはいくつかの異なる情報が含まれていますが、私たちにとって最も興味深く または重要なプロパティはファイル ID です。 この ID を使用すると、アップロードされたファイルを 後で参照できます。したがって、後で いつか、ユーザーは「この画像の中に何が見えますか？」のようなメッセージを送信できます。 そして、この画像ブロックの中には、 実際の画像データの代わりに、 ファイル ID のみを含めることができます。 したがって、ここにファイル ID を含めることができます。 そうすると、Claude は事前にアップロードした画像を 探しに行くことになります。Claude はその後、 画像を可能な限り解釈しようとします。 したがって、ファイル API は、ファイルを事前にアップロードし、 後でリクエストを行い、 リクエストに元のファイルに関する情報を含めることを可能にします。 Claude へ。したがって、これは単に別の方法として考えることができます。 Claude に画像または PDF を提供する方法です。 このファイル API の基本を理解したところで、 つまり、ファイルを送信して 後で参照できるというアイデアを理解したところで、 このビデオのもう 1 つの焦点である コード実行について説明します。コード実行は サーバーベースのツールです。そのため、実装を 提供する必要はありません。行う必要があるのは、 事前定義されたツールのスキーマを提供することだけです。 Claude への最初の要求の中に、 この特別に定義されたツールのスキーマを、 含めたいユーザー送信メッセージと共に含めます。その後、 バックグラウンドで、Claude はオプションで 分離された Docker コンテナ内で Python コードを実行することを選択できます。 Claude は、このコンテナ内で複数回コードを実行できます。 Claude がこれらのコード実行から出力したものはすべて Claude に送信され、Claude は結果を解釈して 最終的な応答を私たちに書き込むことができます。これらの Docker コンテナにはネットワークアクセスはありません。つまり、 Claude はネットワークリクエストを行うコードを 書き出すことも、外部 API にアクセスしようとすることもできません。 代わりに、Docker コンテナに情報を取得し、 そこから情報を取り出すために、 先ほど説明したファイル API と このコード実行ツールを組み合わせて使用します。 それでは、これがどのように機能するかをお見せしましょう。 たとえば、maybe mydata.csv という CSV ファイルがあり、 それに多くの表形式の情報が含まれており、それを Claude に分析してもらいたいとします。 複雑なコード設定で、Claude にコードを 書かせて、それを自分で手動で実行させる代わりに、 ファイル API とコード実行ツールを 組み合わせて使用し、Claude が ファイルを自動的に分析し、結果を生成させることができます。 そのためには、まず ファイル API を使用して CSV ファイルを アップロードします。最初に、ここで CSV ファイルを、その中にいくつかのデータを入れてアップロードします。すると ファイル ID が返ってきます。 次に、そのファイル ID をフォローアップの リクエストに含めます。したがって、 コンテナアップロードブロックと呼ばれるものを追加します。コンテナアップロード ブロックは、以前に Claude にアップロードしたファイルを コンテナ内に注入または配置したいことを意味します。 したがって、タイプがコンテナアップロードで、 ファイル ID プロパティが、元のファイルをアップロードしたときに 取得した ID である、この非常に特別に作成されたブロックを 追加します。次に、別のテキストブロック内で、 Claude に分析を実行するように依頼します。たとえば、 このファイル内のデータを分析するなど、シンプルなものです。 その後、バックグラウンドで、Claude はコード実行ツールを使用します。 Claude は Docker コンテナ内で アップロードされたファイルにアクセスできます。したがって、Claude は ファイルを分析し、結果を処理し、 ファイル内のすべてのデータに関する完全なレポートを 私たちに提供するコードを記述できます。 それでは、このフロー全体の例を見てみましょう。 したがって、005 コード実行と呼ばれるノートブックをまとめました。 また、streaming.csv という別の CSV ファイルも作成しました。 このファイルには、 ビデオストリーミングサービスの多くの偽データが含まれています。 このファイルには、 特定のユーザー、利用中のサブスクリプショントランシェ、 つまり、アクセスレベル、 そしてこの特定のユーザーに関する多くの統計情報が含まれています。 したがって、合計視聴時間、トップジャンルなどです。 さらに、最後の列は 解約済みと呼ばれます。解約済みは、 ユーザーがサブスクリプションをキャンセルしたかどうかを示すものです。 したがって、0 はサブスクリプションをキャンセルしていないことを意味し、1 は キャンセルしたことを意味します。 このファイル内のデータを分析し、 これらのさまざまな機能と、ユーザーがサブスクリプションをキャンセルしたかどうかとの間に 相関関係があるかどうかを把握するために、多くのコードを書くことができます。 しかし、それらすべてを自分でやる代わりに、 このファイル API とコード実行ツールに タスク全体を任せるかもしれません。まず、 この streaming.csv ファイルをアップロードし、 次に Claude にコード実行ツールを使用して すべてのデータを分析するように依頼できます。 それでは、その方法をお見せしましょう。まず、ノートブックに戻って、 ヘルパー関数セルを見てください。 少し下にスクロールすると、 いくつかの異なる関数を追加したことに気付くでしょう。 ファイルパスが与えられた特定のファイルを 自動的にアップロードするアップロード関数を追加しました。 Claude にアップロードしたすべてのファイルを 一覧表示するファイル一覧関数があります。 ファイルを削除したり、ダウンロードしたり、 特定のファイルに関する情報も取得できます。 これらの関数はすぐに使用します。 したがって、そのセルを折りたたみ、もちろん実行することも確認します。 次に、streaming.csv ファイルをアップロードしようとします。 そのセルをすぐに実行します。 ファイルメタデータオブジェクトが返ってきます。 そこに ID があります。それが Claude に対するこのファイルを 識別する一意の ID です。後で会話に含めたい場合は、 その ID を参照します。次に、下のセルでは、 詳細な分析を実行するように Claude に依頼する短いプロンプトがあります。 顧客がサブスクリプションをキャンセルする理由を調べてください。 また、Claude にその調査結果を 要約するグラフを出力するように依頼しています。 その後、 コンテナアップロードブロックがあります。これは実際に アップロードされたファイルをリクエストに含めます。 それでは、セルを実行します。コード実行を使用する際は、 完了するのに少し時間がかかる場合があることに注意してください。 返される応答には膨大な量のテキストが含まれます。 このメッセージには、Claude が作成したすべてのコードと、 その出力、および最終的な分析が含まれます。 Claude はコンテナ内でコードを複数回実行できるため、 このメッセージ内に複数のコードブロックと複数の実行結果が見られる場合があります。 現在、メッセージ内で何が起こっているかを理解するのを助けるために、 そのコンテンツ全体を少しきれいにフォーマットしました。 これがそのメッセージです。 コンテンツリストがあり、さまざまなブロックが含まれています。 最初のブロックはテキストブロックで、 Claude が最初の問題を提示するテキストが含まれています。 Claude はその後、サーバーツール使用ブロックを提供します。 これには、Claude がコンテナ内で実行したいコードが含まれています。 そして、ここにコード実行ツールの結果があります。 コードの実際の実行に関する情報が含まれています。 たとえば、標準出力、標準エラー、 エラー処理が必要な場合の返りコードなどです。 そして、この場合は Claude が さらにコードを実行したようです。 したがって、さらに分析を行い、 さらに結果を取得し、さらに分析を行いました。 このように、この場合は Claude が 徹底的な分析を行うために、コードを複数回連続して実行しました。 このコンテンツをユーザーに表示するかどうかは、 完全に任意であり、取り組んでいるアプリケーションによって異なります。 もしそうしたいなら、非常に見栄えの良いレポートを作成できます。 たとえばこれのようなものです。 したがって、先ほど見ていたすべての情報を取得し、 Claude を使用して非常にきれいにフォーマットしました。 したがって、最初の応答をここで見ることができます。 つまり、最初に受け取ったテキストブロックからの正確な情報です。 次に、コード実行ツールがあります。 Claude が実行することを選択したコードと、 その実行結果があります。そして、これは数回繰り返されているのを見ることができます。 これで、さらにテキストがあります。 別のコード実行があり、同様です。 最後に、最も興味深い側面の 1 つをお見せしたいと思います。 コード実行の。 このプロンプトの中で、 Claude に 1 つの 詳細なグラフを含めるように依頼したことを覚えているかもしれません。 Claude はバックグラウンドでグラフを生成しました。 画像ファイル内で、それは Docker コンテナ内に保存されています。ファイル API を使用して Docker コンテナ内の生成されたグラフを ダウンロードできます。 その方法をお見せしましょう。まず、ここでフォーマットしたメッセージを 詳しく見ていきます。 スクロールしていくと、追加のネストされたコンテンツ プロパティを持つテキストブロックが見つかるかもしれません。 そしてその中に、コード実行出力のタイプが見つかるかもしれません。 ここに私のがあります。 応答内にそれが見つからない場合は、コード実行出力を検索してみてください。 そのすぐ下にファイル ID があります。 このファイル ID を使用してファイルをダウンロードできます。 コピーしてノートブックに戻り、 一番下までスクロールして新しいセルを追加します。 ここです。 ダウンロードファイルと呼ばれる関数を呼び出します。これは ビデオの開始時に見た事前定義された関数の 1 つでした。 そして、先ほど見つけたファイル ID を貼り付けます。 実行します。 正常に実行されます。そして今、私のノートブックと同じ ディレクトリを見ると、 そこに PNG または JPEG ファイルが見つかるはずです。 その名前はランダムになります。厳密にはランダムではありません。 Claude がそれに付けた名前になります。 ファイルを開くと、 Claude が CSV ファイルから抽出した情報が見つかるでしょう。 これは素晴らしい視覚化であり、必要なすべてを教えてくれます。 したがって、解約率と視聴時間、月額料金の範囲で、 など、Claude はこのファイルの内容を理解するのに役立つ 徹底的な分析を行いました。 したがって、このデモからわかるように、 ファイル API とコード実行ツールを組み合わせることで、 より複雑なタスクを Claude に委任できます。 もちろん、データ分析を行うだけに限られません。 コード実行とファイル API の組み合わせを使用して、 さまざまなタスクを実行できます。 そして、それをアプリケーションにどのように統合するかは、完全にあなた次第です。
