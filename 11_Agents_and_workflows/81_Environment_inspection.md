# 81. Environment inspection

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287798
**Section:** 11 Agents and workflows

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Environment inspection
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When building AI agents, one crucial concept often gets overlooked: environment inspection. Claude operates blindly - it needs to be able to observe and understand the results of its actions to work effectively.

Why Environment Inspection Matters

Think about how Claude works with computer use. Every time Claude performs an action like typing text or clicking a button, it immediately receives a screenshot to understand what happened. This isn't just a nice-to-have feature - it's essential.

From Claude's perspective, clicking a button could navigate to a new page, open a menu, or trigger any number of changes. Without being able to see the results, Claude has no way to understand whether its action succeeded or what the new state of the environment looks like.

Reading Before Writing

This same principle applies to file operations. Before Claude can modify any file, it needs to understand the current contents. This might seem obvious, but it's a pattern you should always follow when building agents.

In the example above, when asked to add a new route to a Python file, Claude first reads the existing code to understand the current structure. Only then can it safely make the requested changes without breaking existing functionality.

System Prompts for Environment Inspection

You can guide Claude to inspect its environment through system prompts. For complex tasks like video generation, this becomes especially important.

Consider a video creation agent that needs to:

Generate video content using tools like FFmpeg
Verify that audio dialogue is placed correctly
Check that visual elements appear as expected

You might include system prompt instructions like:

Use the bash tool to run whisper.cpp and generate caption files with timestamps to verify dialogue placement
Use FFmpeg to extract screenshots from the video at regular intervals to visually inspect the output
Compare the generated content against the original requirements

Benefits of Environment Inspection

When Claude can inspect its environment, several things improve:

Better progress tracking - Claude can gauge how close it is to completing a task
Error handling - Unexpected results can be detected and corrected
Quality assurance - Output can be verified before considering a task complete
Adaptive behavior - Claude can adjust its approach based on what it observes

Practical Implementation

When designing your own agents, always ask: "How will Claude know if this action worked?" Whether you're working with files, APIs, or user interfaces, provide tools and instructions that let Claude observe the results of its actions.

This might mean:

Reading file contents before modifications
Taking screenshots after UI interactions
Checking API responses for expected data
Validating generated content against requirements

Environment inspection transforms Claude from a blind executor of commands into an agent that can truly understand and adapt to its working environment.

---

## 🎬 Transcript (English)

The next idea around agents that we are going to discuss is environment inspection. When we were taking a look at computer use previously, you might recall something interesting. After every single action that we saw logged out on the left hand side, like typing or moving the mouse, we always seem to see a screenshot immediately after, and that's what I'm showing you in this diagram right here. Claude, attempted to type out some text, and we see that logged in the first panel up here, and then right after it, we saw a screenshot appear immediately. I'd like you to look at computer use from Claude's perspective. Claude attempts to type or click somewhere and presumably the page is going to change, but Claude doesn't really understand how. Clicking on a button might navigate to a new page or it might open up a menu. In order to understand the result of any action it took, Claude needed a screenshot to understand the new state or the environment that it was in. This same idea holds for any agent that we assemble. After taking inaction, and sometimes before taking inaction, Claude really needs a way of evaluating the result of the action, often beyond whatever just a tool returns. By helping Claude understand its environment, it can better gauge its progress towards completing a task, and also better deal with unexpected results or errors. We can see a very similar idea when we make use of Claude code. So in this screenshot, at the very top, I've asked Claude to update the main.py file. Now, the task I've given Claude here of adding in an additional route is really simple. But before we can ever modify that file in any way, this is going to seem really obvious. Well, Claude needs to understand what the current code is inside the file first. So Claude needs some way of reading the contents of a file. Now again, I know it seems really obvious, but I would encourage you to think about this idea around reading a file before writing to it anytime you're building an agent of your own. This idea is even applicable to our social media video agent. So whenever we make a request off to Claude, we might give it a task like create a video on Python and post it to my social media account, along with our list of tools. Then we might provide some special instructions inside of a system prompt, helping Claude understand how can inspect its environment after generating a video. Personally, if I was relying upon Claude to use FFimPig to generate a video, I would kind of expect it to maybe sometimes make mistakes around the placement of dialogue. So specifically, when audio clips would play, that it generated using some text-to-speech functionality. To help Claude better understand its progress around completing a task when making one of these videos, I might give it some instructions to make use of the BASH tool specifically to run a program called, specifically Whisper CPP. This is a program we can use to generate caption files automatically out of a video. And those caption files have timestamps inside them, so Claude could use this program to make sure the dialog was placed correctly. We might also advise Claude to use the bash tool to run ffimpeg, which has the ability to extract screenshots out of a video. We might tell Claude to extract a screenshot from every second or every 10 seconds, and take a look at the screenshots just to make sure that the video looks as it kind of expects it to look. This allows Claude to inspect the results of its actions, the actual video I created, and make sure that it's completing the task as it should.

---

## 🎬 トランスクリプト（日本語）

次に、エージェントについて議論するアイデアは、 環境の検査です。以前コンピューターの使用について 見ていたとき、何か面白いことを思い出したかもしれません。 左側にログアウトされていた個々の操作の後 たとえば、タイピングやマウスの移動の後、すぐに スクリーンショットが表示されていました。そして それが、ここで示しているダイアグラムです。クロードは テキストを入力しようとし、それが最初のパネルに ログインされているのがわかります。そしてその直後に スクリーンショットが表示されました。クロードの 視点からコンピューターの使用を見てみましょう。クロードは 入力したりどこかをクリックしたりしますが、おそらく ページは変更されるでしょうが、クロードはどのように変更されるか 本当に理解していません。ボタンをクリックすると新しいページに 移動するかもしれませんし、メニューが開くかもしれません。 行った操作の結果を理解するために、クロードは 新しい状態や環境を理解するためにスクリーンショットが 必要でした。この同じアイデアは、私たちが組み立てる どのエージェントにも当てはまります。操作を行った後、 そして時には操作を行う前に、クロードは実際には 操作の結果を評価する方法を必要とします。多くの場合、ツールが 返すもの以上のものです。クロードが環境を理解するのを助けることで、 タスクを完了するための進捗をよりよく測定し、 予期しない結果やエラーにもよりよく対処できます。 クロードコードを利用する際にも、非常によく似た 考え方を見ることができます。このスクリーンショットでは、一番上に main.pyファイルを更新するようにクロードに依頼しました。 ここでクロードに与えたタスク、つまり追加のルートを 追加するというタスクは非常に簡単です。しかし、私たちが そのファイルを変更できるようになる前に、 これは非常に明白に思えるでしょう。クロードは最初に ファイル内の現在のコードを理解する必要があります。だから クロードはファイルを読み取る何らかの方法を必要とします。 これもまた明白に思えるでしょうが、私は あなたがエージェントを構築する際にはいつでも、書き込む前に ファイルを読み取るというアイデアについて考えてみることをお勧めします。 このアイデアは、私たち自身のソーシャルメディアの 動画エージェントにも適用可能です。そのため、私たちが クロードにリクエストを行う際には、Pythonに関する動画を作成して 私のソーシャルメディアアカウントに投稿するというようなタスクを与え、 ツールのリストと一緒に提供するかもしれません。その後、システムプロンプトの中に 特別な指示を提供し、クロードが動画を生成した後に どのように環境を検査できるかを理解するのに役立てるかもしれません。 個人的には、もし私がクロードにFFimPigを使って動画を生成させるなら 、おそらく対話の配置に関して時々間違いを犯すだろうと 予想するでしょう。特に、テキスト読み上げ機能を使って 生成した音声クリップが再生される場合に。 クロードがこれらの動画のいずれかを作成する際のタスク完了の 進捗をよりよく理解するために、私はBASHツールを使って Whisper CPPというプログラムを実行するように指示するかもしれません。これは、動画から 自動的にキャプションファイルを作成するために使用できるプログラムです。そして、それらのキャプション ファイルにはタイムスタンプが含まれているため、クロードは このプログラムを使って対話が正しく配置されていることを確認できます。 また、BASHツールを使ってffimpegを実行するようにクロードに指示するかもしれません。これは、動画から スクリーンショットを抽出する機能を持っています。 私たちはクロードに2秒ごと、または10秒ごとにスクリーンショットを抽出するように指示し、 動画が期待通りの見た目になっていることを確認するために、それらのスクリーンショットを 確認するように指示するかもしれません。これにより、クロードは自分の操作の結果、 実際に作成した動画を検査し、タスクが正しく完了していることを確認できます。 これらの操作の結果を検査し、タスクが正しく完了していることを確認できます。
