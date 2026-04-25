# 08. System prompts

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287733
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    System prompts
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                System prompts are a powerful way to customize how Claude responds to user input. Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case.

Why System Prompts Matter

Consider building a math tutor chatbot. When a student asks "How do I solve 5x + 2 = 3 for x?", you want Claude to act like a real tutor, not just spit out the answer. A good math tutor should:

Initially give hints rather than complete solutions
Patiently walk students through problems step by step
Show solutions for similar problems as examples

You definitely don't want Claude to:

Immediately give direct answers
Tell students to just use a calculator

How System Prompts Work

System prompts provide Claude with guidance on how to respond. You define them as plain strings and pass them into the create function call. The key benefits are:

System prompts provide Claude guidance on how to respond
Claude will try to respond in the same way someone in the specified role would respond
Helps keep Claude on task

Here's the basic structure:

system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)

Seeing the Difference

Without a system prompt, Claude gives a complete step-by-step solution immediately. This might be helpful, but it doesn't encourage the student to think through the problem themselves.

With the math tutor system prompt, Claude's response changes dramatically. Instead of providing the full solution, Claude asks guiding questions like "What do you think would be a good first step to isolate x? Consider what operation we might need to perform on both sides to start moving terms around."

Building a Flexible Chat Function

Rather than hard-coding system prompts, you can make your chat function more reusable by accepting system prompts as parameters:

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

This approach handles an important detail: Claude's API doesn't accept system=None, so you need to conditionally include the system parameter only when it's provided.

Now you can call your chat function with or without a system prompt:

# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)

System prompts are essential for creating AI applications that behave consistently and appropriately for their intended purpose. They transform generic AI responses into specialized, role-appropriate interactions.

---

## 🎬 Transcript (English)

In this video, we're going to take a look at how we can customize the tone and style of response that Claude generates. To help you understand why this is important, I want you to imagine that we are making some kind of math tutor chatbot. So a user will use this chatbot to ask for help in solving math problems. For example, a user might ask for help in solving 5x plus 2 equals 3. Now there's a couple of things that we would want our math tutor to do and a couple of things that we would definitely not want it to do. So for example, we might want Claude to initially only give the students some hints. Maybe just give them a little tip or two in how they might initially approach the problem. And then if the student still doesn't quite understand how to solve the problem, only then maybe walk the student through a solution step by step. We might also want Claude to show solutions for a similar problem to give the student a little bit of inspiration on how they might approach this particular problem. Likewise, there are some things that we would definitely not want Claude to do. For example, we would not want Claude to just immediately respond with a complete answer. And we would also not want Claude to tell the student to just go use a calculator to solve the problem or something like that. So to solve this problem, we're going to use a technique known as system prompting. System prompts are used to customize the style and tone that Claude will respond with. We define a system prompt as a plain string and then pass it into the create function call. The first line of a system prompt will usually assign Claude a role, so we might directly tell Claude that they are a patient math tutor. This will encourage Claude to respond in the same way that a real math tutor was respond. He would probably end up being patient, provide a lot of explanation, but probably not directly answer a student's question. They'll instead guide them to a solution. Now, to see some action, let's go back over to our notebook and see how Claude responds to math questions with and without a system prompt. So back inside of my notebook, I've made a new notebook and I've carried over just our initial client creation and those three helper functions. You do not have to create a new notebook. I'm just letting you know that I did just to organize my code. Then down here inside the next cell, I'm going to ask Claude a very simple question. I'm going to ask it to solve a simple math problem. And we'll see how it initially responds. It will probably just give us a direct answer. And then we'll go back and add in a system prompt to encourage it to give us a little bit more explanation, kind of a tutor approach. So let's see how Claude responds to us without a system message at all. I'm going to make a list of messages. I'll add in a user message to my list of messages. And I'm going to ask it to solve 5x plus 3 equals 2 for x. I'll then get an answer by calling chat with my list of messages and print out the answer. And then if I run the cell, I'm probably going to see an exact step-by-step solution on how to solve this. Now this probably is going to be useful for a student because it's going to show them a step-by-step solution, but it's not quite what we are going for. We want to make a student think, and we want them to arrive at the solution on their own. We just want to give them small steps and kind of guide them in the right direction. So we're going to customize the way in which Claude responds by using a system prompt. Let me show you how we do that. Up inside my chat function, I'm going to make a new variable of system. I'm going to assign to it a multi-line string. And inside there, I'm going to put together a system prompt that I wrote ahead of time. So I'm going to tell Claude that it is a patient math tutor. It should not directly answer student's questions. Instead, give them a little bit of guidance on how to solve the problem. I'm going to make sure that I pass in the system prompt as the system keyword argument to the create function. I'm then going to rerun the cell. I'll then go back down and let's see how Claude responds now. All right, this looks like a much better answer. Rather than just directly telling the student how it's solved the problem, Claude is now prompting the user to go through a solution step by step. Claude is asking the student to first maybe isolate x on one side of the equation and then ask the student how we might go about that. So now we've got a much more interactive experience for the student. And this will help them hopefully help them learn what's going on here a little bit better than just giving them a direct answer. Alright, so clearly using a system prompt is a powerful tool for steering Claude in a particular direction on how it should answer a given user input. Before we move on, I want to do a little bit of a refactor to our chat function. Rather than having a hard-coded system prompt inside of here, I want to be able to specify a system prompt whenever we call the chat function. So in other words, I want to cut this right here, put it down inside the cell underneath, And then I want to be able to pass in a system prompt like so. So now we have a much more reusable chat function that we can use on a wide variety of different problems in the future without having a hard coded system prompt inside of it. So now we need to make sure that we take this system argument and pass it into the create function. Now, doing so is going to require just a little bit more work than you might think. Let me show you why. I'm going to very quickly add in a system keyword argument to the chat function, and I'll default it to be none. If I now run the cell, and then run the cell down here, everything is going to work fine, exactly as expected. However, if I go down to the chat function and I decide that I do not want to provide a system prompt here at all, so if I delete that and then run the cell, I'll end up getting an error message. So we are not allowed to pass in a system prompt of none. So we need to assemble our parameters. We're going to pass into the create function a little bit more dynamically. And if we have a system of none, we do not want to include this parameter at all. So let me show you how we are going to do that with a small refactor. First, I'm going to make a parameter dictionary right above. I'm going to cut and paste in model max tokens and messages. I'm going to convert this to dictionary syntax. So I use double quote, double quote, colons, like so. I'll then check and see if a system prompt was passed in. So if one was passed in, then I want to add it in as the system key inside of the params dictionary, like so. Then I'm going to update the create call down here to star star parameters. And that's it. So now I'm going to rerun that cell. I'll go back down to the next one. And if I call chat without any system keyword argument being passed in, no problem. Everything is going to work just fine. And if I decide that I do want to provide a system prompt, yep, that's going to work just fine as well. OK, so this looks good. So we now got support for a system prompt inside of our chat function.

---

## 🎬 トランスクリプト（日本語）

このビデオでは、Claudeが生成する応答のトーンとスタイルをカスタマイズする方法を見ていきます。 なぜこれが重要なのかを理解していただくために、 何か数学のチューターチャットボットを作っていると想像してみてください。 ユーザーはこのチャットボットを使って、数学の問題を解く手助けを求めます。 例えば、ユーザーは 5x + 2 = 3 を解く助けを求めるかもしれません。 数学のチューターにやってほしいことと、絶対にやってほしくないことがいくつかあります。 例えば、Claudeに最初はヒントだけを与えるようにしたいかもしれません。 問題にどうアプローチすればよいか、少しヒントを与えるだけかもしれません。 そして、もし学生がまだ問題を解く方法を理解していない場合は、 その時になって初めて、ステップバイステップで解法を説明するかもしれません。 また、Claudeに似た問題の解答を示すようにすることもできます。 学生が問題へのアプローチ方法について少しインスピレーションを得られるようにするためです。 同様に、Claudeに絶対にやってほしくないこともいくつかあります。 例えば、Claudeがすぐに完全な解答で応答してしまうのは避けたいです。 また、Claudeが学生に電卓を使って問題を解くように言うのも避けたいです。 そのようなことはしたくありません。 この問題を解決するために、私たちはシステムプロンプトと呼ばれる技術を使用します。 システムプロンプトは、Claudeが応答するスタイルとトーンをカスタマイズするために使用されます。 システムプロンプトをプレーンな文字列として定義し、 それをcreate関数の呼び出しに渡します。 システムプロンプトの最初の行は、通常Claudeに役割を割り当てます。 例えば、Claudeに患者な数学チューターであると直接伝えることができます。 これにより、Claudeは実際の数学チューターが応答する方法で応答するようになります。 彼は患者で、多くの説明を提供しますが、 学生の質問に直接答えることはないでしょう。 代わりに、彼らを解決策に導きます。 それでは、実際に見てみましょう。ノートブックに戻って、 システムプロンプトありとなしで、Claudeが数学の質問にどのように応答するかを見てみましょう。 ノートブックに戻ると、 新しいノートブックを作成し、初期のクライアント作成と 3つのヘルパー関数をすべて持ち込みました。 新しいノートブックを作成する必要はありません。私は 整理のためにそうしたことをお知らせしているだけです。 次に、セルの下に、Claudeに非常に簡単な質問をします。 簡単な数学の問題を解かせます。 そして、どのように応答するかを見てみましょう。おそらく直接的な答えを返すでしょう。 そして、もう少し説明を求めるためにシステムプロンプトを追加しに戻ります。 チューターのようなアプローチです。 システムメッセージなしでClaudeがどのように応答するか見てみましょう。 メッセージのリストを作成します。ユーザーメッセージを メッセージのリストに追加します。そして、 5x + 3 = 2 を x について解くように依頼します。 そして、メッセージのリストでchatを呼び出して応答を取得し、 応答を出力します。 そして、セルを実行すると、おそらくこの解き方をステップバイステップで正確に示すものが見られるでしょう。 これは学生にとって役立つかもしれませんが、 私たちが目指しているものとは少し違います。私たちは学生に考えさせたいのです。 そして、彼らが自分で解決策にたどり着くようにしたいのです。 小さなステップを与えて、正しい方向へ導いてあげたいのです。 そこで、システムプロンプトを使用して、Claudeの応答方法をカスタマイズします。 その方法を説明します。チャット関数の上に、 新しい変数システムを作成します。 複数行の文字列をそれに割り当てます。 そしてその中に、事前に作成したシステムプロンプトを入れます。 Claudeに患者な数学チューターであると伝えます。 学生の質問に直接答えるべきではありません。 代わりに、問題の解き方について少しガイダンスを与えます。 システムプロンプトを システムキーワード引数として渡すようにします。 そして、セルを再度実行します。 次に下に移動して、Claudeがどのように応答するか見てみましょう。 さて、これははるかに良い応答のようです。学生に直接教えるのではなく どうやって問題を解いたか、Claudeは今、 ユーザーにステップバイステップで解法を進めるように促しています。 Claudeは学生に、まずxを分離するように求めています。 方程式の一方の辺に、そして学生にどうするかを尋ねます。 私たちはどのようにそれを行うでしょうか。 これで、学生にとってよりインタラクティブな体験が得られました。 そして、これは彼らがここで何が起こっているのかを 直接的な答えを与えるよりも少し良く理解するのに役立つでしょう。 さて、システムプロンプトを使用することは、 Claudeを指定された方向に誘導するための強力なツールです。 どのようにユーザーからの入力を回答すべきかについて。 次に進む前に、チャット関数のリファクタリングを少し行いたいと思います。 この中にハードコードされたシステムプロンプトを持つのではなく、 チャット関数を呼び出す際にシステムプロンプトを指定できるようにしたいのです。 つまり、ここでこれをカットし、 下に続くセルに貼り付けて、 そして、このようにシステムプロンプトを渡せるようにしたいのです。 これで、将来、 さまざまな問題に広く使用できる、より再利用可能なチャット関数ができました。 ハードコードされたシステムプロンプトを内部に持たずに。 したがって、ここでシステム引数を 取得し、それをcreate関数に渡す必要があります。 そうすることは、あなたが考えるよりも少し多くの作業が必要になります。 なぜそうなのかお見せしましょう。 非常に速くチャット関数にシステムキーワード引数を追加します。 そして、それをデフォルトでNoneにします。 もし今セルを実行し、 そして下のセルを実行すると、すべて正常に機能します。 期待通りです。 しかし、チャット関数に移動して、 ここでシステムプロンプトを提供したくないと判断した場合、 つまりそれを削除してセルを実行した場合、 エラーメッセージが表示されます。 したがって、Noneのシステムプロンプトを渡すことはできません。 そのため、パラメータを組み立てる必要があります。 create関数に少しずつ動的に渡します。そして もしシステムがNoneであれば、私たちは含めたくありません。 このパラメータを全く含めないようにします。 そこで、小さなリファクタリングでそれを行う方法をお見せします。まず、 上にパラメータ辞書を作成します。 モデルと最大トークン、そしてメッセージを カットアンドペーストします。 これを辞書構文に変換します。 ダブルクォート、コロンを使用します。 このように。 そして、システムプロンプトが渡されたかどうかを確認します。 もし一つ渡されたら、それを params辞書のシステムキーとして追加します。 このように。そして ここに作成コールを更新します。 スターパラメータで。 そして、それだけです。 したがって、今あのセルを再実行します。 次のセルに移動します。 そして、システムキーワード引数を渡さずにchatを呼び出した場合、 問題ありません。すべて正常に機能します。 そして、もしシステムプロンプトを提供したいと判断した場合、はい、 それも同様にうまく機能します。 OK、 だからこれは良さそうです。これでシステムプロンプトのサポートが得られました。 チャット関数の中に。
