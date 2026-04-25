# 16. Prompt evaluation

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287731
**Section:** 04 Prompt evaluation

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Prompt evaluation
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques for writing better prompts, while prompt evaluation helps you measure how well those prompts actually work.

Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for crafting effective prompts. It includes techniques like:

Multishot prompting
Structuring with XML tags
Many other best practices

These techniques help Claude understand exactly what you're asking for and how you want it to respond.

Prompt evaluation takes a different approach. Instead of focusing on how to write prompts, it's about measuring their effectiveness through automated testing. You can:

Test against expected answers
Compare different versions of the same prompt
Review outputs for errors

Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

Option 1: Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

Option 2: Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

Option 3: Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective metrics. This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are common traps that all engineers fall into, myself included. It's natural to write a prompt for a serious application and not test it thoroughly enough. We tend to underestimate how many edge cases real users will encounter.

The reality is that when you deploy a prompt to production, users will interact with it in ways you never anticipated. What seemed like a solid prompt during your limited testing can quickly break down when faced with the full variety of real-world inputs.

The Evaluation-First Approach

Option 3 represents a more systematic approach to prompt development. By running your prompt through an evaluation pipeline, you get objective metrics about its performance across a broader range of test cases. This data-driven approach lets you:

Identify weaknesses before they become production issues
Compare different prompt versions objectively
Iterate with confidence based on measurable improvements
Build more reliable AI applications

While this approach requires more upfront investment in time and testing infrastructure, it pays dividends in the reliability and robustness of your final application. The goal is to catch problems during development rather than after your users encounter them.

---

## 🎬 Transcript (English)

Now that we understand how to access Claude, we're going to shift our focus a little bit and look at two new topics, prompt engineering and prompt evaluation. These two topics are all about making sure that we are writing prompts that will get us the best possible output from Claude. Prompt Engineering is a series of techniques that will use any time that we want to write or edit a prompt. These techniques will aid Claude in understanding what we're asking of it and how we want it to respond. Prompt evaluation, on the other hand, is where we do some automated testing of a prompt with a goal of getting some kind of objective metric that tells us if our prompt is effective or not. In this section, we're going to be mostly focused on prompt evaluation. After we understand how to measure the effectiveness of a prompt, we'll then take a look at some prompt engineering techniques. So let's get to it. The first thing I want to do is help you understand where prompt evaluation fits in to the prompt writing process in general. Whenever you first write a prompt, you generally have three different paths ahead of you. Three different ways you can go from there. With option number one, you might take that prompt you put together, maybe test it once or twice and decide it is good enough to use in production. With option number two, you might test the prompt a couple of times with your own custom inputs, and maybe tweak it a little bit to handle a corner case or two that you've noticed. Right away, I want you to understand that options, number one and number two, are kind of traps that all engineers fall into, myself included. It happens to everybody. We all start writing out prompts that are going to eventually be used in serious applications, and we don't really test them enough to make sure that they are working as expected. So whenever you write a prompt, I highly recommend going with option number three. Run your prompt through an evaluation pipeline to get an objective score that will tell you how well your prompt is performing. You can then try to iterate on your prompt a little bit and make sure that it's performing as well as it possibly can.

---

## 🎬 トランスクリプト（日本語）

Claudeへのアクセス方法を理解したので、少し 焦点を移し、プロンプトエンジニアリングとプロンプト評価の2つの新しいトピックを見ていきます。 これら2つのトピックはすべて、Claudeから最良の出力を得るためのプロンプトを 作成することを目的としています。 プロンプトエンジニアリングとは、プロンプトを作成または編集する際に使用する一連のテクニックです。 これらのテクニックは、Claudeが何を求めているか、どのように応答してほしいかを 理解するのに役立ちます。 一方、プロンプト評価とは、プロンプトの自動テストを行い、 プロンプトが効果的かどうかを示す客観的な指標を得ることを目的としています。 このセクションでは、主にプロンプト評価に焦点を当てます。 プロンプトの有効性を測定する方法を理解したら、次にプロンプトエンジニアリングのテクニックをいくつか見ていきます。 それでは始めましょう。まず、プロンプト評価が 一般的なプロンプト作成プロセスにどのように適合するかを理解するのに役立ちます。 プロンプトを最初に作成するときは、通常、3つの異なるパスがあります。 そこから進むための3つの異なる方法です。 オプション1では、作成したプロンプトを一度か二度テストして、 本番環境で使用するのに十分だと判断するかもしれません。 オプション2では、カスタム入力でプロンプトを数回テストし、 注意したエッジケースをいくつか処理するために少し調整するかもしれません。 ここで理解していただきたいのは、オプション1とオプション2は、 すべてのエンジニアが陥る罠であるということです。私自身もそうです。 誰にでも起こります。私たちは皆、最終的に重要なアプリケーションで使用されるプロンプトを書き始めますが、 期待どおりに機能することを確認するために十分にテストしていません。 したがって、プロンプトを作成する際には、オプション3を使用することを強くお勧めします。 プロンプトを評価パイプラインで実行して、プロンプトがどの程度機能しているかを 示す客観的なスコアを取得します。その後、プロンプトを少し反復処理して、 可能な限り最高のパフォーマンスを発揮できるようにすることができます。
