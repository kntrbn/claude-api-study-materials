# 34. Tool schemas

**URL:** https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753
**Section:** 06 Tool use with Claude

---

## 📄 Page Content

Anthropic Academy
    
  

  
    
      Courses
    
  

    

    
      
      

      
        
          My Profile
        
        
      

      
      

      
        Sign Out
      
    
  

  

  

    
    
    
        
            
    
        
    

            
    
        
        
            
                
                    
                        
                            
                                
                            

                            
                                details
                            

                            
                        
                    
                
            
            
                
                
                
                    Tool schemas
                    
                
                
                    
                        
                            
                                
                                    

    
    

    
    
        
            
        
        
            
                
                This video is still being processed. Please check back later and refresh the page.
            
        
        
            
                Uh oh! Something went wrong, please try again.
            
        
    

    

                                
                            
                        
                    
                
            
        
        
            

    
        
            
                
                    
                        
                            
                        
                    
                
            
            
                
                    Summary
                

                

            
        

        
            
                
                    
                        
                            Summary

                            
                                After writing your tool function, the next step is creating a JSON schema that tells Claude what arguments your function expects and how to use it. This schema acts as documentation that Claude reads to understand when and how to call your tools.

Understanding JSON Schema

JSON Schema isn't specific to AI or tool calling - it's a widely-used data validation specification that's been around for years. The AI community adopted it because it's a convenient way to describe function parameters and validate data.

The complete tool specification has three main parts:

name - A clear, descriptive name for your tool (like "get_weather")
description - What the tool does, when to use it, and what it returns
input_schema - The actual JSON schema describing the function's arguments

Writing Effective Descriptions

Your tool description is crucial for helping Claude understand when to use your function. Best practices include:

Aim for 3-4 sentences explaining what the tool does
Describe when Claude should use it
Explain what kind of data it returns
Provide detailed descriptions for each argument

The Easy Way to Generate Schemas

Instead of writing JSON schemas from scratch, you can use Claude itself to generate them. Here's the process:

Copy your tool function code
Go to Claude and ask it to write a JSON schema for tool calling
Include the Anthropic documentation on tool use as context
Let Claude generate a properly formatted schema following best practices

The prompt should be something like: "Write a valid JSON schema spec for the purposes of tool calling for this function. Follow the best practices listed in the attached documentation."

Implementing the Schema in Code

Once Claude generates your schema, copy it into your code file. Here's a good naming pattern to follow:

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)

get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
                "default": "%Y-%m-%d %H:%M:%S"
            }
        },
        "required": []
    }
}

Use the pattern of function_name followed by function_name_schema to keep your schemas organized and easy to match with their corresponding functions.

Adding Type Safety

For better type checking, import and use the ToolParam type from the Anthropic library:

from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    # ... rest of schema
})

While not strictly necessary for functionality, this prevents type errors when you use the schema with Claude's API and makes your code more robust.

---

## 🎬 Transcript (English)

Now that we've got our tool function put together, we are going to move on to step two, which is where we are going to write out a JSON schema. We are going to eventually send all this configuration off to Claude. Claude is going to use it to understand the different tool functions that are available and the different arguments that must be provided to these tool functions as well. The first thing I want you to understand here is exactly what JSON schema is all about. So this entire object you see on the right-hand side, this is not technically a JSON schema per se. Instead, at the very top, there is a name and a description. I'll tell you what those are about in just a little bit. Underneath that, there is a key of input schema. And then assigned to that is that dictionary right there. What I've now highlighted, that is technically what a JSON schema is. So again, let me give you a little bit more background. The idea of JSON schema is not specifically tied to language models or tool calling or anything like that. JSON schema is a data validation specification. So it is a set of rules that can be used to validate any kind of JSON data. So again, it is not specifically tied to language models or tools or anything like that. The language model community decided at some point in time that JSON schema is just a really convenient way of wiring up and handling tool calls. This is a widely understood technology that has been around for many, many years. Now, at this point, I still haven't really explained what the JSON schema spec is all about. So, in total, this thing is used to inform its Claude about the different tools that are available to it. We are going to provide a name for the tool, so in this case it might be GetWeather, and then a description for the tool. This description is meant to tell Claude what the tool does, when to use it, and what kind of data it is going to return. Best practice is to make sure you have a description around three to four sentences long. So even though right here I'm showing only retrieved current weather, in reality, I would definitely want to have a much longer description than this. Then, under this input schema key is going to be the actual JSON schema spec. This is going to describe the different arguments that should be passed into our function. So in this example back over here, if I had a git weather function that received just a location, I would put in input schema with location right here, it needs to be a string, and here's a description of the purpose of that argument. Again, we would want this description of the argument to also be about three to four sentences long, and help Claude understand exactly what this argument controls and how it affects the overall function call. Now, like I mentioned, it might be a little bit intimidating to think that you have to write out all this configuration on your own. Luckily, I've got a trick that is going to help you write out a almost perfect JSON schema spec for every tool you ever put together. So let me show you the trick. First, I'm going to go back over to my editor and I'm going to find our tool function. So for us, it is the get current date time function. I'm then going to take this over to a Claude window. So I'm at Claude.ai here. I'm going to write out a very simple prompt. I'm going to ask Claude to write a valid JSON schema spec for the purposes of tool calling for this function. And then I will also ask Claude to Follow the best practices listed in the attached documentation. Then I'm going to go into put in my tool function, like so. And then here's the real trick. I'm going to go over to the Anthropic API documentation. In the User Guide section, there is a entire page on tool use with Claude. This entire page has a lot of different best practices, and examples of good tool descriptions and bad tool descriptions. So I'm going to just copy all the text here, go back over to my Claude window, paste it in as an attachment and run this. Claude is then going to respond with probably a very strong JSON schema spec. So I'm now going to copy this, take it back over to my editor, and I'm going to paste it in right underneath my existing get current date time function. So I'll say get current date time schema, like so. Now, as a little naming pattern that I like to use here, I'll give my tool function, whatever name I want, and then the schema to match up with it will be underscore schema. So the same name underscore schema. And it makes it a lot easier to keep track of my different schemas. There's one last thing I'm going to do. At the top of the cell, I'm going to add in an import from anthropic.types. I will import tool program. I'm going to take this tool param and wrap it around this entire dictionary. So I'll put in right here, tool param, opening parentheses, and then a closing parentheses down here at the bottom. Adding in this tool param thing is not strictly necessary. In other words, our code is still going to work without it, but it's going to prevent a type error later on when we eventually take this schema and make use of it.

---

## 🎬 トランスクリプト（日本語）

ツール関数を組み立てたので、次に進みます。 ステップ2では、JSONスキーマを記述します。 最終的にはこの構成全体をClaudeに送信します。Claudeは これを使用して、利用可能なさまざまなツール関数と、 これらのツール関数に提供する必要があるさまざまな引数を 理解します。まず、ここで理解してほしいのは JSONスキーマが何であるかということです。 右側にあるこのオブジェクト全体は、 厳密にはJSONスキーマではありません。その代わりに、 一番上には名前と説明があります。 それらが何であるかは、後ほど説明します。その下に input schemaというキーがあり、 それに割り当てられているのが、あの辞書です。 今ハイライトした部分が、厳密にはJSONスキーマです。 JSONスキーマのアイデアは、 特定の言語モデルやツール呼び出しなどに限定されるものではありません。 JSONスキーマはデータ検証仕様です。 つまり、あらゆる種類のJSONデータを検証するために使用できる 一連のルールです。 したがって、これも特定の言語モデルやツールなどに限定されるものではありません。 言語モデルコミュニティは、いつか JSONスキーマがツール呼び出しを処理するのに非常に便利な方法だと判断しました。 これは広く理解されている技術で、長年にわたって存在しています。 さて、この時点で、JSONスキーマの仕様全体について まだ説明していません。そのため、 全体として、これはClaudeに 利用可能なさまざまなツールについて通知するために使用されます。 ツールの名前を提供します。この場合はGetWeatherなどです。 そして、ツールの説明を提供します。この説明は Claudeにツールが何をするのか、いつ それを使用するのか、どのようなデータを返すのかを伝えるためのものです。 ベストプラクティスは、約3〜4文の説明を用意することです。 そのため、ここでは現在の天気情報だけを表示していますが、 実際には、これよりもはるかに長い説明が必要です。その後、 input schemaキーの下には、実際の JSONスキーマ仕様があります。これは、 関数に渡されるべきさまざまな引数を記述するものです。 したがって、この例では、もしlocationだけを受け取る get weather関数を持っていたとしたら、 input schemaにlocationをここに入力します。 それは文字列である必要があり、ここにその引数の目的の説明があります。 再度、引数の説明も約3〜4文にすることをお勧めします。 そして、Claudeがこの引数が何を制御し、 全体的な関数呼び出しにどのように影響するかを 正確に理解できるようにします。 さて、述べたように、自分でこの構成全体を記述するのは少し daunting（気が遠くなる）かもしれません。 幸い、私が作成するすべてのツールにほぼ完璧な JSONスキーマ仕様を作成するのに役立つトリックがあります。 それでは、そのトリックを見せましょう。まず、 エディタに戻って、ツール関数を見つけます。 私たちにとっては、get current date time関数です。 それをClaudeウィンドウに持っていきます。ここではClaude.aiにいます。 非常にシンプルなプロンプトを記述します。 Claudeに、この関数のツール呼び出しのために 有効なJSONスキーマ仕様を記述するように求めます。 そして、添付されているドキュメントに記載されている ベストプラクティスに従うようにClaudeに依頼します。 そして、ツール関数を入力します。 このように。そして、ここが本当のトリックです。 Anthropic APIドキュメントに移動します。 ユーザーガイドセクションには、 Claudeとのツール使用に関する全ページがあります。 この全ページには、多くの異なるベストプラクティスと、 良いツール説明と悪いツール説明の例が含まれています。 なので、ここにすべてのテキストをコピーして、 Claudeウィンドウに戻り、添付ファイルとして貼り付けて実行します。 Claudeは非常に強力なJSONスキーマ仕様で応答するでしょう。 それでは、これをコピーして、エディタに戻り、 既存のget current date time関数の下に貼り付けます。 get current date time schemaと書きます。 このように。 ここで使用する命名規則として、ツール関数に 好きな名前を付け、それに対応するスキーマは アンダースコアスキーマとします。つまり、同じ名前のアンダースコアスキーマです。 これにより、さまざまなスキーマを追跡しやすくなります。 最後のことを1つ行います。 セルの先頭に、anthropic.typesから tool programをインポートします。 このtool paramを取得し、この全体の辞書を囲みます。 なので、ここにtool paramと開き括弧を入れて、 下のほうに閉じ括弧を入れます。 このtool paramを追加することは、必須ではありません。 言い換えれば、これなしでもコードは機能しますが、 このスキーマを実際に使用する際に発生する 型エラーを防ぐことができます。
