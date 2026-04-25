# 31. Introducing tool use

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287747
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Introducing tool use
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Tools allow Claude to access information from the outside world, extending its capabilities beyond what it learned during training. By default, Claude only knows information from its training data and can't access current events, real-time data, or external systems. Tool use solves this limitation by creating a structured way for Claude to request and receive fresh information.

The Problem Without Tools

When users ask Claude for current information, it hits a wall. For example, if someone asks "What's the weather in San Francisco, California?" Claude has to respond with something like "I'm sorry, but I don't have access to up-to-date weather information."

This creates a frustrating user experience when people need real-time data that Claude could theoretically help with if it just had access to current information.

How Tool Use Works

Tool use follows a specific back-and-forth pattern between your application and Claude. Here's the complete flow:

Initial Request: You send Claude a question along with instructions on how to get extra data from external sources
Tool Request: Claude analyzes the question and decides it needs additional information, then asks for specific details about what data it needs
Data Retrieval: Your server runs code to fetch the requested information from external APIs or databases
Final Response: You send the retrieved data back to Claude, which then generates a complete response using both the original question and the fresh data

Weather Example in Practice

Let's see how this works with the weather question. The process becomes much more specific:

When a user asks about current weather, you include instructions in your prompt about how to retrieve weather data. Claude recognizes it needs current information and requests weather data for the specific location. Your server then calls a weather API to get real-time conditions and sends that data back to Claude. Finally, Claude combines the fresh weather data with the user's question to provide an accurate, current response.

Key Benefits

Real-time Information: Access current data that wasn't available during Claude's training
External System Integration: Connect Claude to databases, APIs, and other services
Dynamic Responses: Provide answers based on the latest available information
Structured Interaction: Claude knows exactly what information it needs and how to ask for it

Tool use transforms Claude from a static knowledge base into a dynamic assistant that can work with live data. This opens up possibilities for building applications that need current information, whether that's weather data, stock prices, database queries, or any other real-time information your users might need.

---

## 🎬 Transcript (English)

In this module, we are going to discuss tool use. Tools allow Claude to access information from the outside world. Now, understanding tool use can be a little bit challenging, so in this video, I'm going to give you a really soft introduction. We are going to walk through the entire flow of tool use and understand what it's all about. I want to first begin by giving you an example of where Claude can, unfortunately, sometimes hit its limits. Remember, by default, Claude only has access to information that was actually trained on. So in general, it doesn't really have any information about very recent current events. As an example of this, if we had a user making use of our chatbot, ask a question of something like, what's the weather in San Francisco, California right now? And so if that off to Claude, we would probably get a response back of something like, I'm sorry, but I don't have access to up to date weather information like that. To fix this and give the user a better response, we can make use of tools. Let me show you a diagram that's going to break down tools with really simple terminology. And I'll show you another one that's going to give you an example of how we would solve this specific weather problem. OK, so here's the entire flow that we're going to eventually implement when we start to make use of tools. We're going to send off an initial request to Claude. We're going to ask a question or maybe give Claude a task. And along with that, we're going to include instructions on how Claude can get some extra data from the outside world. Claude will then take a look at whatever question it was asked or whatever task it was given, and it might decide that it needs to ask for some extra data. So it'll send a response back to us where it asks for some extra data, and it's going to give us some details on exactly what information it needs. Then on our server, we are going to run a little bit of code that will go in, get the information that Claude asked for, and then respond with that on a follow-up request back to Claude. Now Claude has all the information it needs in theory to give us a response. So it will generate a final response that will be hopefully augmented or improved by that extra data. Now I'm going to show you the same exact flow, but I'm going to customize each of these little steps for this scenario where a user asks us for some current weather in a particular location. So here's what happened. We would send an initial query off to Claude, and it would include a prompt where the user asks about the weather. And inside of that initial request, we're going to include details on specifically how to retrieve current weather data. Claude would take a look at the prompt and decide, hey, to answer this question, I need to get some current weather data. It send response back to us, where we would then run some code that would reach out to some maybe third party weather API and actually get some live details on what the current weather is for a particular location. Once we have those details from that outside API, we would then make a follow-up request to Claude with that current weather data. And now, Claude has all the information it needs. It has the original prompt along with the up-to-date weather data so it can generate a final response and send it back to us.

---

## 🎬 トランスクリプト（日本語）

このモジュールでは、ツールの使用について説明します。 ツールを使用すると、Claudeは外部の世界から情報を取得できます。 ツールの使用を理解するのは少し難しい場合があるので、このビデオでは、非常に 簡単な紹介をします。ツールの使用全体の 流れをたどり、それが何であるかを理解します。まず Claudeが残念ながら、時々限界に達する可能性のある例を 挙げることから始めたいと思います。 デフォルトでは、Claudeはトレーニングされた情報にしかアクセスできないことを 覚えておいてください。したがって、一般的に、非常に最近の 時事問題に関する情報はほとんどありません。その例として、 チャットボットを利用しているユーザーが、 「今、サンフランシスコの天気はどうですか？」のような質問をしたとします。 そして、その質問をClaudeに投げた場合、 おそらく「申し訳ありませんが、最新の天気情報にはアクセスできません」といった 応答が返ってくるでしょう。これを修正し、ユーザーに より良い応答を提供するために、ツールを使用できます。 ツールの仕組みを非常に簡単な用語で説明する図を 示します。また、この特定の天気の問題をどのように解決するかを示す 別の図も示します。さて、ここに、実際に実装する ツールの使用全体のフローがあります。初期リクエストを Claudeに送信します。質問をしたり、タスクを Claudeに与えたりします。それに加えて、Claudeが外部世界から追加のデータを 取得する方法についての指示を含めます。Claudeは 質問または与えられたタスクを確認し、追加データが必要だと判断するかもしれません。 そのため、追加データを要求する応答を私たちに送信します。 そして、具体的にどの情報が必要かについての詳細を 教えてくれます。その後、私たちのサーバー上で、 Claudeが要求した情報を取得する小さなコードを実行し、 それをClaudeへのフォローアップリクエストで応答します。 これで、Claudeは理論上、応答に必要なすべての情報を持っています。 最終的な応答を生成します。これは、その追加データによって 強化または改善される可能性があります。さて、私は まったく同じフローを示しますが、これらの各ステップを、ユーザーが 特定の場所の現在の天気について質問するシナリオに合わせてカスタマイズします。 では、何が起こったか見てみましょう。初期クエリを Claudeに送信し、ユーザーが天気について質問するプロンプトが含まれます。 そして、その初期リクエスト内に、現在の天気データを 取得する方法に関する詳細が含まれます。Claudeは プロンプトを見て、この質問に答えるためには現在の天気データを取得する必要があると判断します。 そこで、私たちに応答を返します。そこで、私たちは 第三者の天気APIなどにアクセスして、特定の場所の現在の天気に関する実際の 詳細を取得するコードを実行します。その外部APIから その詳細を取得したら、その現在の天気データとともにClaudeにフォローアップリクエストを行います。 これで、Claudeは必要なすべての情報を持っています。元のプロンプトと 最新の天気データの両方を持っているため、最終的な応答を生成して 私たちに送り返すことができます。
