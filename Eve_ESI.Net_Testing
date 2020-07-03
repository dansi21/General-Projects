using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Extensions.Options;
using ESI.NET;
using ESI.NET.Enumerations;
using ESI.NET.Models;
using ESI.NET.Logic;

namespace ConsoleApp2
{
    class Program
    {



        static void Main(string[] args)
        {


            //var url = client.SSO.CreateAuthenticationUrl();
            // Console.WriteLine(url);
            //System.Diagnostics.Process.Start(url);

            //SsoToken token = await _client.SSO.GetToken(GrantType.AuthorizationCode, code);
            //AuthorizedCharacterData auth_char = await _client.SSO.Verify(token);
            test();


            return;
        }

        public static async void test() {

            IOptions<EsiConfig> config = Options.Create(new EsiConfig()
            {
                EsiUrl = "https://esi.evetech.net/",
                DataSource = DataSource.Tranquility,
                ClientId = "",
                SecretKey = "",
                CallbackUrl = "",
                UserAgent = ""
            });

            EsiClient client = new EsiClient(config);



            Console.WriteLine("Test");
            EsiResponse<List<ESI.NET.Models.Universe.ResolvedInfo>> response = client.Universe.Names(new List<long>(){
                1590304510,
                99006319,
                20000006
            }).Result;

            //EsiResponse<long[]> y = client.Universe.Structures().Result;

            //foreach (var f in y.Data)
            //{
            //    Console.WriteLine(f.ToString());
            //}

            EsiResponse<int[]> y = client.Universe.Systems().Result;

            foreach (var f in y.Data)
            {
                //Console.WriteLine(f.ToString());
            }

            int testLong = 30000131;

            EsiResponse<ESI.NET.Models.Universe.SolarSystem> z = client.Universe.System(testLong).Result;

            Console.WriteLine(z.Data.Name);


            EsiResponse<ESI.NET.Models.Universe.IDLookup> a = client.Universe.IDs(new List<string>() { "Drake Ichosira" } ).Result;

            Console.WriteLine(a.Data);

            //long testLong = 1033147547575;

            //EsiResponse<ESI.NET.Models.Universe.Structure> z = client.Universe.Structure(testLong).Result;

            //EsiResponse<List<ESI.NET.Models.Wallet.Transaction>> x = 

            Console.WriteLine(response.Data[0].Name);
            Console.WriteLine(response.Data[1].Name);
            Console.WriteLine(response.Data[2].Name);
            Console.WriteLine(z.Data.ToString());
            Console.ReadLine();
        }
    }
}
