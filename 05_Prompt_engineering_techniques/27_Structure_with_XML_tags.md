# 27. Structure with XML tags

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287741
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Structure with XML tags
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping the sales records in XML tags like <sales_records> and </sales_records>, you create clear delimiters that help Claude understand the structure of your prompt.

Practical Example: Code and Documentation

Here's a more dramatic example of why XML tags matter. If you ask Claude to debug code using provided documentation, mixing everything together creates confusion:

The "Not Great" version makes it nearly impossible to tell what's code versus documentation. The "Better" version uses <my_code> and <docs> tags to create clear boundaries.

Custom Tag Names

You don't need to use official XML tags. Create descriptive names that make sense for your content:

<sales_records> is better than <data>
<athlete_information> clearly identifies user details
<my_code> and <docs> separate different types of content

The more specific and descriptive your tag names, the better Claude can understand the purpose of each section.

When to Use XML Tags

XML tags are most useful when:

Including large amounts of context or data
Mixing different types of content (code, documentation, data)
You want to be extra clear about content boundaries
Working with complex prompts that interpolate multiple variables

Even for shorter content, XML tags can help serve as delimiters that make your prompt structure more obvious to Claude.

Real-World Application

In practice, you might structure a prompt like this:

<athlete_information>
- Height: 6'2"
- Weight: 180 lbs
- Goal: Build muscle
- Dietary restrictions: Vegetarian
</athlete_information>

Generate a meal plan based on the athlete information above.

This makes it crystal clear that the height, weight, goal, and restrictions are all related athlete data that should be considered together when generating the meal plan.

While you might not see dramatic improvements with simple prompts, XML tags become increasingly valuable as your prompts grow more complex and include larger amounts of varied content.

---

## 🎬 Transcript (English)

The next topic we are going to examine is the idea of providing structure in your prompt by using XML tags. Now, let me give you a little bit of backstory on this. Very often, whenever we write out a prompt, we're going to interpolate some amount of content into it. And we've been doing that already. Inside of our example, we have been interpolating some heights, weight, goal, and restrictions. Now each of these values are rather small, but it's entirely possible that we might eventually write a prompt where we need to put in a lot of content into a prompt. For example, examine the prompt on the right-hand side. We might decide to paste in 20 pages of sales records and try to get Claude to analyze them in some way. Whenever we dump a lot of content into a prompt, it can be a little bit challenging for Claude to figure out exactly what text really means what or how text is actually grouped together. One way that we can make the structure of our prompt a little bit more obvious is by wrapping different pieces of content in XML tags. So for example, I might provide a little bit more structure to this prompt on the right by wrapping the sales records right here with an XML tag of sales records. Like so. Now, there is no official XML tag called specifically sales records. This is a name of a tag that I just made up that will probably give Claude a little bit of insight into the nature of the content that exists inside these tags. I could have just as well called this records, or perhaps even data. But of course, being a little bit more specific here is definitely better. So providing a tag of something like sales records would probably get us the best output. Now I want to make sure it's really clear why XML tags like this are necessary. So let me show you a little exaggerated example. In the prompt on the left hand side, I have a leading line of debug my code below using the provided documentation. So this kind of implies two things. It implies that underneath this header statement right here, I have some amount of code that was written by me, that is buggy, and some amount of documentation as well. And if you just look at the code that's listed out here, it's absolutely not very clear what content is the code and what content is the actual documentation. One way that we could clarify this to Claude would be to wrap each chunk of code with appropriate XML tags. For example, on the right-hand side, I might wrap my code with some XML tags that simply say my code being very direct and obvious, and then the code that represents some amount of documentation in a docstag, again, being very clear and obvious. Now it is much easier for Claude to understand what code it is trying to debug and which code provides some source of documentation. Let's take this idea of providing structure via XML tags and try to use it to improve our prompt that we are working on back inside of our notebook. Now, unfortunately in this particular scenario, we don't really have a big blob of content that we really need to delineate in any way. All of our interpolated content like the height, weight, goal, and restrictions are sufficiently short that Claude is probably not going to be confused by them in any way. Regardless, we can still use some XML tags to make it really clear that this is some kind of external input or maybe some information about the athlete that should be considered when generating the meal plan. So we might decide to wrap this entire block right here with some XML tags that just make it really clear that this is information about the athlete. So I might put in tags like athlete information. and then a closing tag on the other side. Now let's try to measure and see whether or not this has any kind of impact on the quality of output. So I'm going to rerun the cell, I'll go down to my eval cell and run this one. And then you might recall that before adding in those XML tags, I had a score of 7.3. So let's see if we go up or down. And I end up going up quite a bit. Now, you probably not going to see an improvement quite this large. As a reminder, I'm using a little bit more simple and basic model just so I get some exaggerated returns in these improvements to the prompt. So if you do not see quite a big a jump in quality, that is totally fine.

---

## 🎬 トランスクリプト（日本語）

次に検討するトピックは、XMLタグを使用したプロンプトの構造化という考え方です。 XMLタグを使用してプロンプトに構造を提供するという考え方です。 それでは、これに関する背景情報を少しお話しします。非常に 多くの場合、プロンプトを作成する際には、ある程度の コンテンツをそこに挿入します。そして、それはすでに実施しています。 例の中では、身長、体重、目標、そして 制限事項をいくつか挿入してきました。これらの値はそれぞれ 小さいですが、完全に可能性があります。私たちは 最終的に、プロンプトに多くの コンテンツを挿入する必要があるプロンプトを作成するかもしれません。例えば、 右側のプロンプトを見てみましょう。20ページにわたる販売記録を貼り付けて、 20ページにわたる販売記録を貼り付けて、 それをClaudeに分析させようとするかもしれません。 プロンプトに多くのコンテンツを投入すると、 Claudeが正確に把握するのが少し難しくなることがあります。 どのテキストが何を意味するのか、または テキストがどのようにグループ化されているのか。一つの方法として、 プロンプトの構造をもう少し明確にすることができます。 さまざまなコンテンツをXMLでラップすることによって タグでラップします。例えば、右側のこのプロンプトに もう少し構造を与えたいかもしれません。この右側のプロンプトに 販売記録をXMLでラップして 販売記録というタグを付けます。 このように。さて、 「販売記録」という公式なXMLタグは 特に存在しません。これは私がちょうど作った タグの名前で、Claudeにコンテンツの性質について いくらかの洞察を与えるでしょう。 「記録」や、あるいは「データ」と呼ぶこともできたでしょう。しかし、もちろん、 「記録」や、あるいは「データ」と呼ぶこともできたでしょう。しかし、もちろん、 ここに具体的に記述することは間違いなく より良いでしょう。したがって、「販売記録」のようなタグを提供すると、 おそらく最高の出力を得られるでしょう。さて なぜこのようなXMLタグが必要なのかを本当に明確にしたいです。 そこで、少し誇張された例をお見せしましょう。左側のプロンプトでは、 左側のプロンプトでは、 「提供されたドキュメントを使用して、以下のコードをデバッグしてください」という 先頭の行があります。これは2つのことを意味します。 これは、このヘッダー文の直下に、 私が書いたバグのあるコードと、 ドキュメントの量があることを意味します。そして、もしあなたが ここにリストされているコードだけを見ると、 どのコンテンツがコードで、 どのコンテンツが実際のドキュメントなのかは、まったく明らかではありません。 それをClaudeに明確にする一つの方法は、 コードの各チャンクを適切なXMLタグでラップすることです。 例えば、右側では私のコードを 「私のコード」というシンプルなXMLタグでラップするかもしれません。 「私のコード」というシンプルなXMLタグでラップするかもしれません。 非常に直接的で分かりやすく、そしてドキュメントを表すコードは 「docstag」で、これも非常に明確で分かりやすいです。 「docstag」で、これも非常に明確で分かりやすいです。さて Claudeがどのコードをデバッグしようとしているのか、そしてどのコードが ドキュメントのソースを提供しているのかを理解するのがはるかに容易になりました。 XMLタグを介して構造を提供するというこの考え方を 取り上げて、私たちのノートブックで作業しているプロンプトを改善するために 使用してみましょう。残念ながら、この特定のシナリオでは、 私たちが区別する必要のある大きなコンテンツの塊は実際にはありません。 私たちが区別する必要のある大きなコンテンツの塊は実際にはありません。 私たちが区別する必要のある大きなコンテンツの塊は実際にはありません。 私たちの挿入されたコンテンツ、つまり身長、体重、 目標、制限事項はすべて十分に短いため、Claudeは それらに混乱することはないでしょう。それにもかかわらず、 これらのコンテンツが外部からの入力であること、または アスリートに関する情報であることを明確にするために、 これらのコンテンツが外部からの入力であること、または 食事プランを生成する際に考慮されるべきアスリートに関する情報であることを明確にするために、 これらのアスリートに関する情報であることを明確にするために、このブロック全体をXMLタグでラップすることを検討します。 これらのアスリートに関する情報であることを明確にするために、このブロック全体をXMLタグでラップすることを検討します。 アスリートに関する情報であることを明確にするために、このブロック全体をXMLタグでラップすることを検討します。 アスリート情報と 閉じタグを反対側に付けます。さて、 出力の質に何らかの影響があるかどうかを測定してみましょう。 セルの実行を再開します。評価セルに移動して このセルを実行します。XMLタグを追加する前に 7.3というスコアがあったことを覚えているかもしれません。 どれくらい上がるか、下がるか見てみましょう。 かなり上がりました。 これほど大きな改善は見られないかもしれません。 念のため、私は少し単純で基本的な モデルを使用しているので、誇張された結果を得ることができます。 これらのプロンプトの改善点。したがって、もし これほど大きな品質の向上が見られない場合は、全く問題ありません。
