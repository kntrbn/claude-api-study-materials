# 80. Agents and tools

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287803
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Agents and tools
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Agents represent a shift from the structured workflows we've been working with. While workflows are perfect when you know the exact steps needed to complete a task, agents shine when you're not sure what those steps should be. Instead of defining a rigid sequence, you give Claude a goal and a set of tools, then let it figure out how to combine those tools to achieve the objective.

This flexibility makes agents attractive for building applications that need to handle varied, unpredictable tasks. You can create an agent once, ensure it works reasonably well, and then deploy it to solve a wide range of problems. However, this flexibility comes with trade-offs in reliability and cost that we'll explore later.

How Tools Make the Agent

The real power of agents lies in their ability to combine simple tools in unexpected ways. Consider a basic set of datetime tools:

get_current_datetime - Gets the current date and time
add_duration_to_datetime - Adds time to a given date
set_reminder - Creates a reminder for a specific time

These tools seem simple individually, but Claude can chain them together to handle surprisingly complex requests:

For "What's the time?", Claude simply calls get_current_datetime. But for "What day of the week is it in 11 days?", it chains get_current_datetime followed by add_duration_to_datetime. For setting a gym reminder next Wednesday, it might use all three tools in sequence.

Claude can even recognize when it needs more information. If you ask "When does my 90-day warranty expire?", it knows to ask when you purchased the item before calculating the expiration date.

Tools Should Be Abstract

The key insight for building effective agents is providing reasonably abstract tools rather than hyper-specialized ones. Claude Code demonstrates this principle perfectly.

Claude Code has access to generic, flexible tools like:

bash - Run any command
read - Read any file
write - Create any file
edit - Modify files
glob - Find files
grep - Search file contents

It notably doesn't have specialized tools like "refactor code" or "install dependencies." Instead, Claude figures out how to use the basic tools to accomplish these complex tasks. This abstraction allows it to handle countless programming scenarios that the developers never explicitly planned for.

Best Practice: Combinable Tools

When designing agents, provide tools that Claude can combine in creative ways. For example, a social media video agent might include:

bash - Access to FFMPEG for video processing
generate_image - Create images from prompts
text_to_speech - Convert text to audio
post_media - Upload content to social platforms

This tool set enables both simple workflows (create and post a video) and more interactive experiences where the agent might generate a sample image first, get user approval, then proceed with video creation.

The agent can adapt its approach based on user feedback and preferences, something that would be difficult to achieve with a rigid workflow. This flexibility is what makes agents powerful for building dynamic, user-responsive applications.

---

## 🎬 Transcript (English)

Now that we have taken a look at several different workflows, we are going to pivot and start to discuss agents. Understanding agents is easiest if you think back to workflows, specifically when we would actually use them. Workflows were most effective when we knew the precise series of steps required to complete a given task. Agents, on the other hand, are more effective when we don't really know exactly what steps are required. So in these scenarios, we give Claude a task and a set of tools. And then we rely upon Claude to create a plan to complete the task using the given tools. This flexibility around agents is what makes them really attractive for building. The thought process is that you can make an agent, make sure it works reasonably well, and then the agent can solve a wide variety of different tasks. However, there are some major drawbacks to this approach, which we will discuss in a little bit. A key aspect of agents is their ability to make use of tools in different combinations. So to help you understand this, I want to think back to an earlier example that we went through earlier on inside this course, where we put together three different tools. We created tools like Get Current Date Time, Add duration to Date Time, and Set Reminder. Each of these tools were rather simple in nature, but Claude was able to combine them in different, kind of surprising ways to achieve a wide variety of different tasks that we might not really have planned out ahead of time. Let me show you some examples. So on the left hand side of this diagram, I've got some example tasks that we could feed into Claude along with those three different tools. And then on the right hand portion is a series of different tool calls that Claude might make to complete the given task. So for example, if we ask Claude what's the given time, easy enough, Claude can just call the get current date time tool by itself and answer the question. If we ask Claude what day of the week is in 11 days, it could first call get current date time and then add duration to date time. If we ask Claude to say, set a reminder to go to the gym next Wednesday, Claude could first figure out the current day of the week, add a duration onto it, and then set a reminder for that particular day. Finally, Claude can also figure out when it needs some extra information in order to successfully call a tool. So if a user asks, when does my 90-day warranty expire? Well, there's really no guarantee that the user got the warranty today. So Claude might first ask the user for a bit of extra information, particularly when they actually obtain the warranty. Once the user gives them that information, then Claude can call add duration to date time and figure out when the warranty will expire. These are all examples of ways in which Claude can take a set of tools and combine them together in an interesting fashion in order to solve a given task. And this is going to lead us into our first big lesson or understanding around agents. And that is that the set of tools we provide to an agent need to be a reasonably abstract. And a great example of this and to help you understand what I really mean hereby abstract is to go back and look at Claude code and specifically some of the tools that are provided to it. Claude Code gets access to a very small set of abstract tools. And when I say abstract, I mean generic or general or kind of vague in purpose. They are not hyper specialized in any way. So Claude Code gets access to tools like Bash in order to run commands, web fetch to fetch URL, write to create a file, and so on. And Claude Code can figure out how to modify and add features to an existing codebase in really amazing ways by combining together these different tools. Claude Code does not have access to hyper-specialized tools that just fulfill one very specific task in one specific scenario. So for example, on the right-hand side of this diagram, these are all tools that Claude Code notably does not have. So there is no refactor tool that will just magically refactor a file. Instead, Claude Code should figure out how to make use of the tools on the left-hand side in order to refactor something. Likewise, there is no install dependencies tool. Instead, Claude Code needs to read files to understand the project configuration and then run the bash tool to run the appropriate command to install the dependencies. The lesson that we can take from this is that whenever we create an agent, we want to make sure that we provide reasonably abstract tools that Claude can somehow figure out how to piece together in order to achieve some goal. So for example, if we go back to our example of building some kind of social media video creation agent, we might provide it for different tools. One might be Bash, which would give it access to FFmpeg. That's a commonly used CLI tool that you can use to generate videos, given some input images or videos or text or audio and so on. We might also give it a generate image tool, a text to speech tool, just to augment the video generation process, and then finally, a post media tool so that it can take the generated content, whatever it made, and post that content to a social media account. Claude can use that set of tools in rather unexpected ways. So for example, it would enable a flow like what you see on the left-hand side, where a user might chat with our agent and ask it to create and post a video on Python programming. But this set of tools might also allow for more dynamic interactions with the user. For example, on the right-hand side, a user might ask for a video, but first ask the agent to generate a sample cover image to use in the video. Then our agent could first generate an image, show it to the user, get the user's approval, and then go into the video generation process.

---

## 🎬 トランスクリプト（日本語）

いくつかの異なるワークフローを見てきたので、 これから方向転換して、エージェントについて議論します。エージェントを 理解することは、ワークフローを思い出すと最も簡単です。特に、 実際にそれらを使用した場合です。ワークフローは、 指定されたタスクを完了するために必要な手順の正確な系列を知っている場合に 最も効果的でした。それに対して、エージェントは、 必要な手順が正確にわからない場合に、より効果的です。 したがって、これらのシナリオでは、 Claudeにタスクとツールのセットを与えます。そして、 Claudeが与えられたツールを使用してタスクを完了するための計画を作成することを 期待します。エージェントのこのような柔軟性が、 ビルドにおいて本当に魅力的である理由です。思考プロセスは、 エージェントを作成し、それが合理的にうまく機能することを確認してから、 エージェントがさまざまなタスクを解決できるようにすることです。しかし、 このアプローチにはいくつかの大きな欠点があり、 それは少し後に議論します。エージェントの重要な側面は、 さまざまな組み合わせでツールを利用する能力です。 したがって、これを理解するために、以前の例を思い出してほしいのですが、 このコースの早い段階で行った、3つの異なるツールを組み合わせて、 Get Current Date Time、Add duration to Date Time、 Set Reminderのようなツールを作成しました。これらの各ツールは 比較的シンプルでしたが、Claudeはそれらを異なる、 ある意味驚くべき方法で組み合わせて、 事前に計画していなかった可能性のあるさまざまなタスクを達成することができました。 いくつか例を示します。 この図の左側には、Claudeとこれら3つの 異なるツールに渡すことができるサンプルタスクがいくつかあります。 そして、右側には、Claudeがタスクを完了するために行う可能性のある さまざまなツール呼び出しの系列があります。 例えば、Claudeに現在の時刻を尋ねると、 それは簡単です。Claudeは Get Current Date Time ツールを単独で呼び出し、 質問に答えることができます。Claudeに11日後の曜日を尋ねると、 最初に Get Current Date Time を呼び出し、 次に Add duration to Date Time を呼び出すことができます。 Claudeに次回の水曜日にジムに行くリマインダーを設定するように頼むと、 Claudeはまず現在の曜日を把握し、それに期間を追加してから、 リマインダーを設定できます。最後に、 Claudeは、ツールを正常に呼び出すために追加の情報が必要な場合を特定することもできます。 ユーザーが「90日間の保証はいつ失効しますか？」と尋ねたとします。 ユーザーが今日保証を取得したという保証はありません。 したがって、Claudeはまずユーザーに追加情報を依頼するかもしれません。 特に、いつ保証を取得したか。ユーザーがその情報を提供すると、 Claudeは Add duration to Date Time を呼び出し、 保証がいつ失効するかを把握できます。これらはすべて、 Claudeがツールのセットを取得して、 さまざまな興味深い方法でそれらを組み合わせて、 指定されたタスクを解決する方法の例です。 そして、これはエージェントに関する私たちの最初の大きなレッスンや理解につながります。 それは、エージェントに提供するツールのセットが かなり抽象的である必要があるということです。 そして、これを理解するのに役立つ良い例は、 Claude Codeに戻って、特にそれに提供されている ツールのいくつかを見ることです。 Claude Codeは、非常に小さな抽象ツールのセットにアクセスします。 そして、私が抽象と言うとき、私は 目的において汎用的または一般的またはやや曖昧であるという意味です。 それらはまったく特殊化されていません。 したがって、Claude Codeは、コマンドを実行するためのBash、 URLをフェッチするための Web Fetch、ファイルを作成するための Write などにアクセスします。 Claude Codeは、これらの異なるツールを組み合わせることで、 既存のコードベースを変更して機能を追加する方法を、 非常に素晴らしい方法で見つけ出すことができます。 Claude Codeは、非常に特定のタスクを 1つの特定のシナリオで実行するだけの、特殊化されたツールにはアクセスしません。 したがって、例えば、この図の右側にあるのは、 Claude Codeが特に持っていないすべてのツールです。 そのため、ファイルを魔法のようにリファクタリングするリファクタリングツールはありません。 代わりに、Claude Codeは左側のツールを使用して、 何かをリファクタリングする方法を見つける必要があります。 同様に、依存関係をインストールするツールもありません。代わりに、 Claude Codeは、プロジェクト構成を理解するためにファイルを読み込み、 次に Bash ツールを実行して、依存関係をインストールするための適切なコマンドを実行する必要があります。 ここから得られる教訓は、エージェントを作成する際には、 Claudeが目標を達成するために何らかの方法でそれらをまとめる方法を見つけることができる、 かなり抽象的なツールを提供することを 確認したいということです。 例えば、ソーシャルメディアビデオ作成エージェントのようなものを構築するという 例に戻ると、4つの異なるツールを提供するかもしれません。 1つは Bash で、FFmpeg にアクセスできるようにします。これは 入力画像、動画、テキスト、音声などからビデオを生成するために使用できる、 一般的な CLI ツールです。 また、画像生成ツール、テキスト読み上げツールも提供して、 動画生成プロセスを補強するかもしれません。 そして最後に、メディア投稿ツールを提供して、 作成した生成コンテンツをソーシャルメディアアカウントに投稿できるようにします。 Claudeは、これらのツールのセットを、 ある意味予期しない方法で使用できます。 例えば、左側にあるようなフローを可能にします。 ユーザーがエージェントとチャットして、 Python プログラミングに関するビデオの作成と投稿を依頼するかもしれません。 しかし、このツールのセットは、よりダイナミックな ユーザーとのやり取りも可能にするかもしれません。 例えば、右側では、 ユーザーが動画を要求するかもしれませんが、まずエージェントに 動画で使用するサンプルカバー画像を生成するように依頼するかもしれません。 その後、私たちのエージェントは画像を生成し、 ユーザーに表示し、ユーザーの承認を得てから、 ビデオ生成プロセスに進むことができます。
