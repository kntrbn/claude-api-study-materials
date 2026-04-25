# 32. Project overview

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287751
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Project overview
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

The goal is straightforward: we want to be able to tell Claude "Set a reminder for my doctor's appointment. It's a week from Thursday" and have Claude respond with "OK, I will remind you." But to make this work, we need to address some limitations in how Claude handles time and reminders.

Why This Is Challenging

While Claude knows the current date, there are three specific problems we need to solve:

Limited time awareness: Claude might know the current date, but not the exact time
Date calculation issues: Claude doesn't always handle time-based addition well, especially when looking many days into the future
No reminder capability: Claude doesn't know how to set a reminder - it has no built-in mechanism for this

Each of these limitations represents a gap between what Claude can do naturally and what we need for our reminder system. Tools are how we bridge these gaps.

Tools We Need

We'll create three separate tools to handle each challenge:

Get the current date time: Claude needs to know the current date and time precisely
Add duration to date time: Claude isn't perfect with date time addition, so we'll give it a reliable tool for this
Set a reminder: We need a way to actually set a reminder in the system

We'll implement these tools one at a time, starting with the simplest one. This approach lets us understand how tool calling works before building more complex functionality. By the end, Claude will be able to handle natural language requests like "remind me in a week" by combining these tools to calculate the exact time and set the reminder.

This project demonstrates a key principle of working with AI: when the model has limitations, we extend its capabilities through tools rather than trying to work around those limitations in our prompts.

---

## 🎬 Transcript (English)

To learn more about tools, we are going to set ourselves a little goal. This is going to be a small project that we implement inside of a Jupyter notebook. We are going to try to teach Claude how to set reminders that occur at some point in time in the future. This is going to require us to implement several different tools. And right now, we're just going to focus on one tool at a time, but just know that we're going to eventually have to deal with multiple tools. So I want to eventually be able to send a message to Claude of something like, set a reminder for my doctor's appointment, it's a week from Thursday. And I want Claude to respond to something like, okay, I will remind you at that point in time. When you first look at this task, you might think it seems really easy, but it turns out that there are actually several different challenges that we're going to need to tackle, and we're going to solve all of them through the use of tools. So in particular, Claude does know the current date. In other words, if you open up a prompt right now, you could ask it what the current date is and it will give you an exactly correct answer. However, Claude doesn't always know the exact time of day. So if we were to ask Claude to do something like set a reminder for 24 hours from now and expecting it to be exactly 24 hours, Claude doesn't really know what 24 hours from now actually is because it doesn't know the current time. Secondly, Claude does not always perfectly handle time-based addition. So if I were to ask it, what is 379 days from January 13, 1973? Claude will very often give you the correct answer, but sometimes it will get that addition incorrect. And finally, Claude just doesn't know what it means to set a reminder, as no concept of it. It does know conceptually what setting a reminder is, but there's no mechanism inside of Claude whatsoever for setting reminders in the future. To solve each of these issues, we are going to make a dedicated tool. So we have three issues right here. We are going to make three separate tools, one at a time. Here's what each tool is going to do. We're going to have a very simple tool that we're going to get started with. It's going to help us understand what tool calling is all about. Its only job is to get the current date time. So that means the current date plus the time. The second tool we will make will add a duration to a date time. So this will allow us to say something like take the current date and add 20 days to it and what would the resulting day be. And then finally, we will make a reminder setting tool as well.

---

## 🎬 トランスクリプト（日本語）

ツールについて学ぶために、私たちは 小さな目標を設定します。これは、私たちが実装する小さなプロジェクトになります Jupyter notebook内で。私たちは Claudeにリマインダーを設定する方法を教えようとします 将来のある時点で発生する。これは いくつかの異なるツールを実装する必要があります。 そして今、私たちは一度に1つのツールに焦点を当てます。 しかし、最終的には複数のツールを扱う必要が出てくることを知っておいてください。 なので、私は最終的にClaudeにメッセージを送れるようになりたいと思っています 「リマインダーを設定して」といったようなものです。 来週の木曜日です。 そして、Claudeには「承知しました。」のような返答をしてほしいです。 その時間に思い出させます。 このタスクを最初に見たとき、それは非常に簡単だと思われるかもしれませんが、 実際にはいくつかの異なる課題があることがわかります。 それらをすべてツールを使って解決します。 特に、Claudeは現在の日付を知っています。つまり、 現在の日付を知っています。 例えば、今プロンプトを開いて現在の日付を尋ねると 正確に正しい答えを返してくれます。 しかし、Claudeは常に正確な時間までを知っているわけではありません。 例えば、「今から24時間後に」というようなことを頼むと ちょうど24時間後にリマインダーを設定して そしてそれがちょうど24時間であると期待しても Claudeは「今から24時間後」が実際に何であるかを知りません なぜなら、現在の時刻を知らないからです。 第二に、Claudeは 時間に基づいた加算を常に完璧に処理できるわけではありません。 例えば、「1973年1月13日から379日後はいつですか？」と尋ねると Claudeはしばしば正しい答えを返しますが、時には その加算を間違えることがあります。そして 最後に、Claudeはリマインダーを設定するということが何を意味するのかを知りません。 概念としてはリマインダーを設定することが何を意味するのかは知っていますが Claude自体にリマインダーを設定するメカニズムは全くありません。 概念的にはリマインダーを設定することが何を意味するのかは知っていますが Claude自体にリマインダーを設定するメカニズムは全くありません。 これらの問題のそれぞれを解決するために、私たちは専用のツールを作成します。 したがって、ここに3つの問題があります。私たちは3つの 別々のツールを作成します。一度に1つずつ。 各ツールが何をするかです。私たちは非常に 簡単なツールから始めます。それは ツール呼び出しについて理解するのに役立ちます。その 唯一の仕事は現在の日時を取得することです。つまり 現在の正確な日付と時刻です。 次に作成する2番目のツールは、日付に期間を加えます。 日付に。これにより、 例えば、「現在の日付に」と言えるようになります。 20日を加えたらどうなるか。 そして最後に、リマインダー設定ツールも作成します。
