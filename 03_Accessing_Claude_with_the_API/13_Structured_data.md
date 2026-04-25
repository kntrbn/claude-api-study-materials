# 13. Structured data

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287732
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Structured data
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text around your content. While this is usually great, sometimes you need just the raw data with nothing else.

Consider building a web app that generates AWS EventBridge rules. Users enter a description, click generate, and expect to see clean JSON they can immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks with explanatory text, users can't simply copy the entire response - they have to manually select just the JSON portion.

The Problem with Default Responses

By default, when you ask Claude to generate JSON, you might get something like this:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

This rule captures EC2 instance state changes when instances start running.

The JSON is correct, but it's wrapped in markdown formatting and includes explanatory text. For a web app where users need to copy the raw JSON, this creates friction in the user experience.

The Solution: Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])

This technique works by:

The user message tells Claude what to generate
The prefilled assistant message makes Claude think it already started a markdown code block
Claude continues by writing just the JSON content
When Claude tries to close the code block with ```, the stop sequence immediately ends generation

The result is clean JSON with no extra formatting:

{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}

Processing the Response

You might notice some extra newline characters in the response. These are easy to handle:

import json

# Clean up and parse the JSON
clean_json = json.loads(text.strip())

Beyond JSON

This technique isn't limited to JSON generation. Use it anytime you need structured data without commentary:

Python code snippets
Bulleted lists
CSV data
Any formatted content where you want just the content, not explanations

The key is identifying what Claude naturally wants to wrap your content in, then using that as your prefill and stop sequence. For code, it's usually markdown code blocks. For lists, it might be different formatting markers.

This approach gives you precise control over Claude's output format, making it much easier to integrate AI-generated content into applications where clean, structured data is essential.

---

## 🎬 Transcript (English)

stop sequences, and assistant message prefilling can be combined together in a really powerful way. Something that you're probably going to end up doing rather frequently, anytime you need to generate some kind of structured data. So to help you understand how these things work together, we'll me walk you through a really quick example. Let's imagine that we are building a web app like the one you see on the screen. This is a web app that's going to generate event bridge rules based upon some user input. If you're not familiar with them, event bridge rules are used in AWS, they're essentially little JSON snippets. So, user is going to enter in some prompt like this and then click on generate. In chances are, the user is going to want to see some generated rule just up here that they can very easily select right away or click on this little copy button and go use somewhere else. The point there is that part of the critical user experience here is that we want to show just the JSON for the generated rule and nothing else. So if we instead displayed a response that looks like this, it would definitely not be as helpful for our users. We're still generating the rule, but now it also has this header up top and this commentary footer down at the bottom. So now a user can't really use this copy all button. They would have to go in and manually select that JSON right there. So this is an example where we really don't want Claude to be that helpful and explains work. We want just some very particular data and nothing else. Now to be clear, this is not a problem that is just limited to generating JSON. It turns out that any time you are using Claude to generate any kind of structured data. So it could be JSON, or it could be Python, or even just a bulleted list of text items. Claude is very often going to try to insert a header or a footer or some additional kind of commentary. And in many of these scenarios, you don't want that additional commentary. You just want the raw content that you asked Claude to create. So to help keep Claude on track here and only give us the raw content we're asking for and no additional header or footer or commentary or anything like that, we can use our stop sequence in combination with a pre-filled assistant message. Let me show you how. I'm going to go back over to my notebook. I'm going to continue on by making a new cell down here. I'm going to again make a list of messages. I'll add in a user message. I'll say something like generate a very short event ridge rule as Jason. I'll then pass that off like so, and then let's just see what we get with this kind of initial take. So right away, we can see that we do get back some JSON, but it has unfortunately that little back tick, back tick, back tick, JSON right there, and then a matching closing one over there. And just to make sure it's super clear, these back ticks are in place to format this all as markdown. So it gets formatted very nicely if you were to render it as markdown text. But in our case, we don't want any of those additional characters. We want just the raw JSON by itself. So to do so, we can do two things. We're going to use both an assistant message and a stop sequence. For right now, we're just going to write out the code to do so. And then I'll show you a diagram that explains how it all works. First, I'm going to pre-fill an assistant message. So let's say add assistant message. And my pre-fill message will be backtick, backtick, backtick, JSON. And then on my chat call, I'll add in stop sequences. And anytime we see a back tick, back tick, back tick, I want to immediately stop generation. So let's now run the cell and see what we get back. Okay, so now we get just the JSON by itself. You will notice that there are some new line characters in here, but that's totally fine. We can very easily remove those extra new lines by just parsing the response as JSON or by doing a strip call. So I could say text is chat. I'll print out text and then on the next cell down, I might import JSON and do a JSON loads with text and strip on text as well. And if I run that, yes, we definitely get back some very well-formatted JSON here that we can access in any way that we expect. All right, so what exactly is going on with the assistant message and the stop sequence? Well, let me show you diagram just to break it all down and make sure it is super clear. So once again, we are doing our user message. We're providing a pre-filled assistant and a stop sequence. Claude is going to take a look at all the different parts of this request. It's going to initially take a look at that user message content and say, all right, it's very clear that I need to write a full rule. And I should probably also describe it. So maybe put on a header and a footer because that's kind of what Claude naturally wants to do. It wants to explain the work that is doing. But then it's going to encounter that assistant message. And just as we learned in the last video, Claude is going to assume that it already wrote that out in its response. So it's going to say, oh, I've already started the JSON part. So now all I have to do is write out the actual JSON. It's then going to write out all of this JSON in the response. And then as it gets to the very end, it's going to naturally want to close off that markdown code block that it thought it created earlier. So Claude is going to want to put in a closing backtick, backtick, backtick. As soon as it does so, however, it's going to encounter the stop sequence, which stops the generation entirely and immediately sends us back the response. So you can really imagine that what's really going on here is we're kind of saying, start with this and with that and just give us everything in between. And that results in us just getting back the part we really care about, just the JSON by itself. And like I mentioned, this is a really powerful technique that we're going to use very often. Anytime we want to generate some kind of structured data and get just that data with nothing else besides it. And remember, this technique can be used for any kind of structured data. It is not limited just being used on JSON. So anytime we have any kind of very specific content we want to generate and get just that content with no additional commentary on it, we're going to take a look at using assistant message prefilling along with stop sequences.

---

## 🎬 トランスクリプト（日本語）

ストップシーケンスとアシスタントメッセージの事前入力 は、非常に強力な方法で組み合わせることができます。 これは、構造化データを作成する際には頻繁に 行うことになるでしょう。ですので、 これらの機能がどのように連携するかを理解するために、 非常に簡単な例を紹介します。例えば、 画面で見ているようなWebアプリを構築しているとしましょう。これは、 ユーザーの入力に基づいてEventBridgeルールを生成するWebアプリです。 EventBridgeルールに慣れていない場合は、AWSで使用され、 基本的に小さなJSONスニペットです。したがって、 ユーザーはこのようなプロンプトを入力し、「生成」をクリックします。 そして、ユーザーは生成されたルールをここに表示して、 簡単に選択したり、この小さなコピーボタンをクリックして どこかで使用したりしたいと思うでしょう。 そこで重要なのは、ここでの重要なユーザーエクスペリエンスは、 生成されたルールのJSONのみを表示したいということです。 それ以外は何も表示したくありません。したがって、 もしレスポンスがこのように表示されたら、ユーザーにとっては はるかに役立たなくなるでしょう。私たちはまだルールを生成していますが、 今度は上部にヘッダー、 下部にコメントが付いています。したがって、 ユーザーはコピーボタンを効果的に使用できません。 手動でJSONを選択する必要があります。 ですから、これはClaudeに説明の作業を させたくない例です。非常に特定のデータだけが欲しいのです。 それ以外のものは不要です。明確にしておくと、 これはJSON生成に限定された問題ではありません。 Claudeを使用して構造化データを作成する場合は常に、 JSON、Python、あるいは単なる箇条書きのテキストアイテムなど、 Claudeはヘッダー、フッター、またはその他の コメントを挿入しようとします。そして、これらのシナリオの多くでは、 追加のコメントは不要です。 Claudeに作成を依頼した生のコンテンツだけが必要です。 したがって、Claudeをこのままにして、要求した生のコンテンツのみを 提供してもらうには、ヘッダー、フッター、 またはその他のコメントを付けずに、 ストップシーケンスと事前入力されたアシスタントメッセージを 組み合わせて使用できます。その方法を示します。 ノートブックに戻ります。 下に新しいセルを作成して続けます。 メッセージのリストを再度作成します。 ユーザーメッセージを追加します。 「短いEventBridgeルールをJSONで生成してください」と書きます。 次にそれを渡します。 そして、この最初の試みで何が得られるか見てみましょう。 すぐにJSONが得られますが、残念ながら バックスラッシュ、バックスラッシュ、バックスラッシュ、JSONと 表示されています。そして、対応する閉じのバックスラッシュもあります。 そして、それが非常に明確であることを確認するために、 これらのバックスラッシュはマークダウンとしてフォーマットするために あります。つまり、マークダウンテキストとしてレンダリングすると、 非常にきれいにフォーマットされます。しかし、私たちの場合は、 これらの追加の文字は必要ありません。 単独で生のJSONが必要です。ですので、 2つのことを行います。アシスタントメッセージとストップシーケンスを 両方使用します。まずは、 それを行うためのコードを記述します。その後、 どのように機能するかを説明する図を示します。 まず、アシスタントメッセージを事前入力します。 「アシスタントメッセージを追加」と言います。 そして、事前入力メッセージはバックスラッシュ、バックスラッシュ、 バックスラッシュ、JSONとなります。そして、 チャットコールでストップシーケンスを追加します。 バックスラッシュ、バックスラッシュ、バックスラッシュが見えたら すぐに生成を停止したいのです。 それではセルを実行して、 何が得られるか見てみましょう。 はい、これでJSONだけが得られました。 ここにいくつかの改行文字が含まれていることに気づくかもしれませんが、それはまったく問題ありません。 これらの余分な改行は、レスポンスをJSONとして解析するか、 stripコマンドを実行することで簡単に削除できます。 したがって、次のように言うことができます。 テキストはチャットです。テキストを出力し、 次のセルでJSONをインポートし、 テキストとストリップを実行します。 テキストも同様です。それを実行すると、 はい、確かに非常に適切にフォーマットされたJSONが得られました。 これにより、予想通りにアクセスできます。 さて、アシスタントメッセージとストップシーケンスで具体的に何が起こっているのでしょうか？ 図で説明して、非常に明確に理解できるようにしましょう。 もう一度、ユーザーメッセージを行っています。 事前入力されたアシスタントとストップシーケンスを提供しています。 Claudeは、このリクエストのすべての部分を確認します。 まずユーザーメッセージの内容を確認し、「ルール全体を 書く必要があることは明らかです。 おそらく説明も加えるべきでしょう。」と考えるでしょう。 ヘッダーやフッターを付けるのが、Claudeが自然に行いたいことだからです。 Claudeは、行っている作業を説明したいのです。 しかし、アシスタントメッセージに出くわすと、 前のビデオで学んだように、 Claudeはそれをすでに応答に含めたと想定します。 したがって、「ああ、JSONの部分はすでに開始した。」と考え、 今は実際のJSONを書くだけです。 そして、このJSON全体を応答に記述します。 そして、一番最後になると、 以前作成したと思ったマークダウンコードブロックを 自然に閉じようとします。 したがって、Claudeは終了のバックスラッシュ、バックスラッシュ、 バックスラッシュを入れようとします。それが完了するとすぐに、 ストップシーケンスに遭遇します。 これにより、生成が完全に停止し、すぐにレスポンスが返されます。 したがって、実際に行われていることは、 「これ」で開始し、「あれ」で終わらせ、 その間のすべてを提供するように指示しているようなものです。 その結果、私たちが本当に気にかけている部分、 つまりJSONだけが得られます。 そして申し上げたように、これは非常に強力なテクニックであり、 私たちはそれを頻繁に使用します。構造化データを作成し、 それ以外は何もない、そのデータだけを取得したい場合はいつでもです。 そして、このテクニックはあらゆる種類の構造化データに使用できることを覚えておいてください。 JSONで使用されることに限定されません。 したがって、非常に特定のコンテンツを作成したい場合で、 そのコンテンツに付随するコメントなしで、それだけを取得したい場合は、 アシスタントメッセージの事前入力と ストップシーケンスの使用を検討します。
