# 24. Prompt engineering

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287745
**Section:** 05 Prompt engineering techniques

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                                
                                    
                                    2
                                    download
                                
                            
                        
                    
                
            
            
                
                
                
                    Prompt engineering
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves iterative refinement - starting with a basic prompt, evaluating its performance, then systematically applying engineering techniques to improve it.

The Iterative Improvement Process

The approach follows a clear cycle that you can repeat until you achieve your desired results:

Set a goal - Define what you want your prompt to accomplish
Write an initial prompt - Create a basic first attempt
Evaluate the prompt - Test it against your criteria
Apply prompt engineering techniques - Use specific methods to improve performance
Re-evaluate - Verify that your changes actually improved the results

You repeat the last two steps until you're satisfied with the performance. Each iteration should show measurable improvement in your evaluation scores.

Setting Up Your Evaluation Pipeline

To demonstrate this process, we'll work with a practical example: creating a prompt that generates one-day meal plans for athletes. The prompt needs to take into account an athlete's height, weight, goals, and dietary restrictions, then produce a comprehensive meal plan.

The evaluation setup uses a PromptEvaluator class that handles dataset generation and model grading. When creating your evaluator instance, you can control concurrency with the max_concurrent_tasks parameter:

evaluator = PromptEvaluator(max_concurrent_tasks=5)

Start with a low concurrency value (like 3) to avoid rate limit errors. You can increase it if your API quota allows for faster processing.

Generating Test Data

The evaluation system can automatically generate test cases based on your prompt requirements. You define what inputs your prompt needs:

dataset = evaluator.generate_dataset(
    task_description="Write a compact, concise 1 day meal plan for a single athlete",
    prompt_inputs_spec={
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg", 
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions of the athlete"
    },
    output_file="dataset.json",
    num_cases=3
)

Keep the number of test cases low (2-3) during development to speed up your iteration cycle. You can increase this for final validation.

Writing Your Initial Prompt

Start with a simple, naive prompt to establish a baseline. Here's an example of a deliberately basic first attempt:

def run_prompt(prompt_inputs):
    prompt = f"""
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    return chat(messages)

This basic prompt will likely produce poor results, but it gives you a starting point to measure improvement against.

Adding Evaluation Criteria

When running your evaluation, you can specify additional criteria that the grading model should consider:

results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    extra_criteria="""
The output should include:
- Daily caloric total
- Macronutrient breakdown  
- Meals with exact foods, portions, and timing
"""
)

This helps ensure your prompt is evaluated against the specific requirements that matter for your use case.

Analyzing Results

After running an evaluation, you'll get both a numerical score and a detailed HTML report. The report shows you exactly how each test case performed, including the model's reasoning for each score.

Don't be discouraged by low initial scores - a score of 2.3 out of 10 is typical for a first attempt. The goal is to see consistent improvement as you apply engineering techniques.

The d

---

## 🎬 Transcript (English)

Now that we've got a handle on prompt evaluation, we're going to move on to the world of prompt engineering. Remember, prompt engineering is all about taking a prompt we've written and improving it in some way to get more reliable outputs and higher quality outputs. To understand prompt engineering, we're going to go through a series of videos in this module, and I want to very quickly help you understand how the module is set up. In this video and the next, we're going to write out an initial prompt. And then in the coming videos, we're going to try to improve it step by step by implementing new prompt engineering techniques on that original prompt. So in short, in this video, we're going to set a goal. So something we want our prompt to do, we're then going to write an initial version of that prompt. So kind of like a really poor first attempt. We will then eval the prompt, and then we're going to see right away we get a very poor evaluation score. And then as I mentioned in the coming videos, we're going to learn about and apply some different prompt engineering techniques. And as we apply each of these, we're going to run our evaluation again and see that we are getting better performance with every single improvement we make. Now to run these evals, we're going to use that same kind of eval pipeline that we put together in the previous module. Just one little twist here, something you really need to be aware of if you want to follow along and code with me. I took our original eval pipeline that we put together in the last module, and I made a couple of different improvements to it to make sure that it can work with just about any prompt, as opposed to the very specific prompt we were working on previously. So to get this updated notebook that has this more flexible evaluation pipeline, make sure you download the accompanying notebook named 001 underscore prompting. Before you open up that notebook, however, I want to very quickly tell you about the goal of our prompt. So this initial prompt that we're going to write and exactly what it is intended to do. All right, so we're gonna make a prompt that's going to hopefully generate a one-day meal plan for an athlete based upon their height, weight, some kind of physical goal that they might have, and any dietary restrictions they might have. So you can imagine that we are going to take in some kind of sample input that describes an athlete. Maybe there are height, weight, goal, and dietary restrictions. We're then going to interpolate all those inputs into our prompt. And then we're going to send that off to our model. And hopefully we'll get back some kind of output, like what you see on the right-hand side. This is what we're really going for. This is our ideal output. In the first version of our prompt, we're going to get some output that looks nothing like what you see here on the right-hand side, but through a variety of different prompt-entering techniques, we're going to eventually refine the prompt and eventually hopefully get something that looks almost exactly like this. All right, so now that we understand our goal, let's open up that new notebook. So remember, 001 prompting. I can give you a very quick tour of it because there are a couple of things have changed compared to the last module. And just make sure everything inside there is super clear. We'll then use the notebook to generate our initial data set. All right, so I've opened up that notebook. Right away, you'll notice there are a couple of collapsed cells at the top. So this is a lot of different setup code. Just make sure you execute those cells at least one time. So I can do so right away. Next up, you'll see that I'm creating an instance of something called a prompt evaluator. Prompt evaluator is a class I created that wraps up all the data set generation, all the model grading, just about everything is wrapped up inside of this class. The class takes one argument, max concurrent tasks. So this class supports concurrency. We can make multiple API calls at the same time. The upside to this is that it's going to dramatically speed up our eVal process and the data set generation process as well. But I do need you to be aware that depending upon your service quota, you may or may not very quickly start to run into some rate limit errors. So if you see any rate limit errors at all, as you go through this module, I would highly encourage you to change this value right here all the way down to the default of one. which means no concurrency at all. For me personally, I have super high rate limits. So I'm going to dial this all the way up to a concurrency of 50. Chances are you are not going to be able to use 50. So don't try 50. I would really recommend maybe starting off at three. And then if you see any rate limit errors, start to go down to two or one. Again, I'm going to use 50 just so you can see some immediate feedback on my screen as I run all these different steps. I'm going to make sure I run that cell. And then let's get started on generating our actual data set. So to generate the data set, I've added this new generate data set method for us. To use this method, we're going to describe the overall purpose of our prompt. So kind of what our prompt is supposed to do. For you and I, we're trying to work on a prompt that is going to write a compact, concise, one day meal plan for a single athlete. And then inside of this prompt input spec, we're gonna have a dictionary that's gonna list out all the different inputs that our prompt requires. As we saw just a moment ago, our prompt is gonna require a height, a weight, a goal, and some dietary restrictions. So these are some extra properties that are gonna be generated as a part of the data set. And eventually we're gonna take them, test case by test case, and interpolate them into our prompt. So I'm gonna fill out all four of these different properties. My height is going to be the height in CM and just be clear I'll put in athlete's height. And I'm going to duplicate that because it's going to be just about the same. We're going to do our weight in kilograms. My goal is going to be the goal of the athlete and my restrictions will be a dietary restrictions of the athlete. And the last input for you to be aware of is number of test cases to generate. I would really recommend that you just leave this at three because it's going to allow you to get through this module way faster because the eVals are going to run much more quickly. Just remember, as I mentioned many times whenever we do an eVal in reality, we want to have a really solid, really large number of test cases. So I'm going to dial mine personally way up. I do not recommend you do this. I recommend you leave it at like two or three, just to make sure all your evals run very quickly. But again, I'm going to dial mine all the way up to 50. Once I put this all together, I'm going to run the cell and that's going to generate my data set. Once I have generated my data set, I can open up the data set.json file, which should be created in the same directory. And we're going to see all these different individual data sets have been generated. So they have a pretty similar structure to what we were doing on our previous module when we were talking about prompt eVals. I'm going to go back over to my notebook and then scroll down a little bit to the run prompt function. This is where we are going to write out our prompt and then eventually improve it over time. This function gets called one time for every test case that you generated. Whenever this function is called, it's going to receive your test cases prompt inputs as its only argument. So in other words, prompt inputs right there is going to be that dictionary. And then that function is going to be called again, and it will be that dictionary, and then again, and it will be that dictionary and so on. So we're going to take this dictionary and we're going to interpolate those inputs into this prompt that we're going to write out right here. Let's immediately write out a first version of our prompt. And it's going to be very simple, very naive. We're going to get a very bad eval score, but it will at least get us started. So I'm going to write in my initial starting frontier and I'm going to use a very bad prompt. I'll say, what should this person eat? And then I'm going to list out their height. their weight, their goal, and dietary restrictions. And then for each of these, I'm going to interpolate in a value from prompt inputs. So the first one will be the height. And I'm going to copy paste that just a save a little bit of time and update the keys on each one. So make sure you have first height and then we want the weight and then our goal and then restrictions. All right, once we have our starter prompt in here, I'm going to run that cell. And then let's do our eVal. So we can run our eVal down here at the very bottom. Now, before we run our eVal, I want you to know that this function that's going to actually kick off the evaluation process, it takes in one additional keyword argument that I'm not showing here. It's called extra criteria. It's going to be a string. This string is going to be used during the model grading process. This extra criteria thing just allows you and I as developers to put in some extra criteria that the model should consider whenever it's doing some grading. So I'm going to say specifically to make sure that the output should include a daily caloric total, a macro nutrient breakdown. and meals with exact foods, portions, and timing. Again, this is just going to add in a little bit of extra validation or a little bit of extra grading criteria. All right, so now let's run our evaluation for the first version of our prompt and see how we're doing. All right, we get a absolutely terrible score. I get a 2.32. Now, just you know, you are probably going to end up getting a much better score than I get. The reason I have a very bad score here is that I'm using a model since that is not super smart. So it's going to tend to give me really bad output unless I'm very specific in how I prompt it. I am using this very bad model just so you can see the increase in score over time as we go throughout this module and add in all these different prompt engineering techniques. So again, you are probably going to get a better score. That's totally fine. Now, before we move on, there's one last thing I want to mention really quickly. Whenever you run any valuation, a file will be created in the same directory as your notebook called output.html. If you open up that file inside of your browser with a simple drag and drop, you're going to see a really nicely formatted report that gives you output on every single test case that was executed along with the score, the reasoning, solution criteria, and so on. And you can also see the actual output too. So I'm going to use this little dashboard quite a bit in order to take a look at the output of the Eval and understand how I actually need to improve my prompt. All right, I apologize for the long video here, but now hopefully you have an idea of some of the setup that we're doing inside of this module. So now all we really have to do, as you can see, we have really bad score right now. All we have to do is start to improve our prompt. So let's start to take a look at our first prompt engineering technique in the next video.

---

## 🎬 トランスクリプト（日本語）

プロンプト評価について理解したので、次はプロンプトエンジニアリングの世界に進みます。プロンプト エンジニアリングとは、作成したプロンプトを改善して、より信頼性の高い出力と高い 品質の出力を得ることを目的としています。プロンプトエンジニアリングを理解するために、 このモジュールでは一連のビデオを視聴します。そして、モジュールがどのように構成されているかを 素早く理解していただきたいと思います。このビデオと次のビデオでは、最初の プロンプトを作成します。そして、その後のビデオでは、元のプロンプトに 新しいプロンプトエンジニアリング技術を適用して、ステップバイステップで改善していきます。 つまり、このビデオでは目標を設定します。つまり、プロンプトに何をさせたいか。 そして、その初期バージョンを作成します。非常に悪い最初の試みのようなものです。 その後、プロンプトを評価し、すぐに非常に悪い評価スコアが得られることを確認します。 そして、お伝えしたように、今後のビデオでは、さまざまなプロンプトエンジニアリング技術を 学び、適用していきます。そして、それぞれを適用するたびに、評価を実行し、 改善を行うたびにパフォーマンスが向上していることを確認します。これらの評価を実行するために、 前のモジュールで作成したのと同じような評価パイプラインを使用します。 ここで少しだけひねりがあります。一緒にコードを書きたい場合は、この点に注意する必要があります。 前のモジュールで作成した元の評価パイプラインを使い、 以前に作業していた特定のプロンプトだけでなく、ほぼすべてのプロンプトで動作するように いくつかの異なる改善を加えました。したがって、このより柔軟な評価パイプラインを備えた 更新されたノートブックを入手するには、001_promptingという名前の付随するノートブックをダウンロードしてください。 そのノートブックを開く前に、プロンプトの目標について簡単に説明したいと思います。 つまり、最初のプロンプトとその目的です。さて、私たちは、アスリートの身長、体重、 身体的な目標、および食事制限に基づいて、 アスリート向けの1日の食事プランを生成するプロンプトを作成する予定です。 例えば、アスリートの身長、体重、目標、食事制限を記述したサンプル入力を取得し、 それらの入力をプロンプトに挿入し、モデルに送信して、右側に表示されているような 出力を得られるようにします。これが私たちの理想的な出力です。プロンプトの最初のバージョンでは、 右側にあるものとは全く似ていない出力を得ますが、さまざまなプロンプトエンジニアリング手法によって、 最終的にプロンプトを改善し、これとほぼ同じものになるようにします。 さて、目標を理解したので、新しいノートブックを開きましょう。001_promptingを覚えておいてください。 前のモジュールから変更された点がいくつかあるので、簡単なツアーを提供できます。そして、 内部のすべてが非常に明確であることを確認します。次に、このノートブックを使用して、 実際のデータセットを生成します。さて、ノートブックを開きました。すぐに、上部にいくつか の折りたたまれたセルがあることに気付くでしょう。これは多くのセットアップコードです。 少なくとも一度はこれらのセルを実行してください。すぐに実行できます。次に、 プロンプト評価者のインスタンスを作成しています。プロンプト評価者は、データセットの生成、モデルの採点、 ほぼすべてをラップするクラスです。このクラスは、最大同時タスクという1つの引数を取ります。 このクラスは並列処理をサポートしています。同時に複数のAPI呼び出しを行うことができます。 これにより、評価プロセスとデータセット生成プロセスの両方が劇的にスピードアップします。 しかし、サービス割り当てによっては、レート制限エラーに非常に早く遭遇する可能性があることを 認識していただく必要があります。したがって、このモジュールでレート制限エラーが発生した場合は、 この値をデフォルトの1に下げることを強くお勧めします。つまり、並列処理はありません。 個人的には、レート制限が非常に高いので、50の並列処理に設定します。 おそらく50を使用できないでしょう。したがって、50を試さないでください。3から始めることをお勧めします。 そして、レート制限エラーが発生した場合は、2または1に下げてください。 繰り返しになりますが、私は50を使用します。これにより、私の画面で即座にフィードバックを確認できます。 これらのすべてのステップを実行します。セルを実行し、実際のデータセットの生成を開始しましょう。 データセットを生成するために、この新しいgenerate_datasetメソッドを追加しました。このメソッドを使用するには、 プロンプトの全体的な目的を記述します。つまり、プロンプトが何をすべきかということです。 あなたと私は、アスリートの身長、体重、目標、食事制限に基づいて、コンパクトで簡潔な1日の食事プランを 作成するプロンプトに取り組んでいます。そして、prompt_input_spec内に、 プロンプトが必要とするすべての異なる入力をリストする辞書があります。 少し前に見たように、プロンプトには身長、体重、目標、食事制限が必要です。 これらはデータセットの一部として生成される追加のプロパティであり、最終的にはテストケースごとに それらをプロンプトに挿入します。したがって、これら4つのプロパティすべてを埋めます。 私の身長はセンチメートル単位の身長です。明確にするために、アスリートの身長を入力します。 そして、ほぼ同じなので複製します。キログラム単位で体重を測定します。 私の目標はアスリートの目標です。 そして私の制限はアスリートの食事制限です。 最後の入力は、生成するテストケースの数です。3にすることをお勧めします。 これにより、このモジュールをはるかに速く進めることができます。評価がはるかに速く実行されるためです。 繰り返しますが、評価を行う際には、本当に堅固で本当に多数のテストケースが必要です。 そのため、個人的には数値を大幅に増やします。あなたにはお勧めしません。 2または3に設定することをお勧めします。これにより、すべての評価が非常に迅速に実行されることを確認できます。 しかし、繰り返しますが、私は50を使用します。これをすべてまとめると、セルを実行します。 そして、データセットが生成されます。データセットを生成したら、同じディレクトリに作成されるはずの dataset.jsonファイルを開き、個々のデータセットがすべて生成されていることを確認できます。 前のモジュールでプロンプト評価について話していたときに行ったものと非常に似た構造になっています。 ノートブックに戻り、もう少し下にスクロールして、run_prompt関数に移動します。 ここでプロンプトを作成し、時間の経過とともに改善していきます。この関数は、 生成された各テストケースに対して1回呼び出されます。この関数が呼び出されると、 テストケースのプロンプト入力を唯一の引数として受け取ります。 つまり、prompt_inputsは辞書になります。そして、その関数が再び呼び出され、 その辞書となり、そしてまた呼び出され、その辞書となり、以降も同様です。 したがって、この辞書を取得し、ここで作成するプロンプトにそれらの入力を挿入します。 すぐにプロンプトの最初のバージョンを作成しましょう。非常にシンプルで、非常に素朴です。 非常に悪い評価スコアを得ますが、少なくとも開始できます。したがって、 私の最初の開始フロンティアを書き込みます。非常に悪いプロンプトを使用します。「この人は何を食べるべきか？」と尋ねます。 そして、彼らの身長、体重、目標、食事制限をリストします。 そして、これらのそれぞれについて、prompt_inputsの値から値を挿入します。 最初のものは身長です。少し時間を節約するためにコピー＆ペーストし、各キーを更新します。 したがって、まず身長があることを確認し、次に体重、目標、そして制限が必要です。 を開始プロンプトをここに入力したら、セルを実行します。 そして、評価を行いましょう。評価はここで、一番下で実行できます。 評価プロセスを開始する関数を実行する前に、ここで表示していない追加のキーワード引数があることを知っておいてください。 それはextra_criteriaと呼ばれます。これは文字列です。 この文字列は、モデルの採点プロセス中に使用されます。 このextra_criteriaというものは、開発者である私が、モデルが採点を行う際に考慮すべき 追加の基準をいくつか設定できるようにするものです。具体的には、 出力に毎日のカロリー合計、主要栄養素の内訳、正確な食品、ポーション、タイミングを含む べきであることを確認します。これは、少し追加の検証または追加の採点基準を追加するだけです。 さて、プロンプトの最初のバージョンの評価を実行し、どのように進んでいるかを確認しましょう。 ひどいスコアが出ました。2.32です。ご存知のように、あなたは私よりもはるかに良いスコアを得るでしょう。 私が非常に悪いスコアを持っている理由は、あまり賢くないモデルを使用していることです。 したがって、プロンプトが非常に具体的でない限り、悪い出力を与える傾向があります。 この非常に悪いモデルを使用しているのは、このモジュールを通してスコアの増加を 見ることができるようにするためです。そして、これらのさまざまなプロンプトエンジニアリング技術をすべて追加していきます。 したがって、繰り返しになりますが、あなたは良いスコアを得るでしょう。それは全く問題ありません。 次に進む前に、もう一つ非常に簡単に言いたいことがあります。 評価を実行するたびに、ノートブックと同じディレクトリにoutput.htmlというファイルが作成されます。 そのファイルをブラウザでドラッグ＆ドロップで開くと、 実行されたすべてのテストケースの出力と、スコア、理由、ソリューション基準などを 提供する非常にうまくフォーマットされたレポートが表示されます。実際の出力も確認できます。 したがって、この小さなダッシュボードを多く使用して、評価の出力を確認し、 プロンプトを改善する方法を理解します。さて、長いビデオになってしまいましたが、 これで、このモジュールで行っているセットアップの一部を理解できたはずです。 ですから、今私たちが行う必要があるのは、ご覧のとおり、非常に悪いスコアが出ています。 プロンプトを改善し始めるだけです。次のビデオで最初のプロンプトエンジニアリング技術を見ていきましょう。
