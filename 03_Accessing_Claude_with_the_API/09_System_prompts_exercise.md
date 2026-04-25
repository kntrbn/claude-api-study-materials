# 09. System prompts exercise

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287724
**Section:** 03 Accessing Claude with the API

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
            
                
                
                
                    System prompts exercise
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.

---

## 🎬 Transcript (English)

Let's go through a quick exercise on system prompts. I've updated my notebook and I'm now asking Claude to write out a Python function that is going to check a string for duplicate characters. If I run this and print out the answer, I'm going to see a tremendous amount of code gets generated here. So some of it is going to be a little bit of code, but there's also going to be a lot of explanation and a lot of comments as well. So I would like to go through an exercise here where we try to reduce the amount of code that's being generated. I want to get down to as concise and implementation of this function as possible. To do so, I would like you to write out a system prompt and pass it into the chat function call. Your system prompt should assign a role to Claude and encourage it to respond as concisely as possible. So again, go ahead and pause the video here, go ahead and give it a shot, and we'll go over solution right about now. To solve this, I'm going to pass in a system prompt to the chat function call. And inside that, I'm going to assign a role to Claude that will encourage it to write very concise code. I'll say you are a Python engineer who writes very concise code. So let's now run the cell and see what kind of response we get back now. All right, that is definitely much more in line with what I was looking for. You'll see that the actual code we had to write to implement this uniqueness check is very, very short, much shorter than the code we saw a moment ago. Hopefully you had some success with this exercise. And if you didn't, that is totally fine. There are going to be many other exercises throughout the course where you can test out your skills.

---

## 🎬 トランスクリプト（日本語）

システムプロンプトに関する簡単な演習を行いましょう。 ノートブックを更新し、Claudeに文字列をチェックする Python関数を書くように求めています。 これを実行して回答を印刷すると、膨大な量のコードが生成されるのがわかります。 つまり、その一部は少しのコードになりますが、説明もたくさんあります。 コメントもたくさんあります。 そこで、生成されるコードの量を減らすための演習を行いたいと思います。 この関数の実装をできるだけ簡潔にしたいのです。 そうするために、システムプロンプトを書いてチャット関数呼び出しに渡したいと思います。 あなたのシステムプロンプトはClaudeにロールを割り当て、 できるだけ簡潔に回答するように促す必要があります。 ですので、もう一度、ここで動画を一時停止して試してみてください。 それでは、ここでソリューションを見ていきましょう。 これを解決するために、システムプロンプトをチャット関数呼び出しに渡します。 そしてその中で、Claudeに非常に簡潔なコードを書くように促すロールを割り当てます。 あなたは非常に簡潔なコードを書くPythonエンジニアです、と言います。 それでは、セルを実行してどのような応答が得られるか見てみましょう。 さて、それは確かに私が求めていたものに、より近くなりました。 このユニークさのチェックを実装するために書く必要があった実際のコードを見ると、 数分前見たコードよりもはるかに短くなっています。 この演習がうまくいったことを願っています。もしそうでなくても、全く問題ありません。 コース全体を通して、スキルを試すことができる演習は他にもたくさんあります。 。 。 。 。 。 。 。 。 。
