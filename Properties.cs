using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConfiguratorToParser
{
    class Properties
    { 
        public bool? isEnableBroadcastToAccounts { get; set; }
        public bool? isEnadbleSchedudler { get; set; }
        public Account? Account { get; set; }
        public string? Genre { get; set; }
        public string? NameOfLastAlbum { get; set; } = "";
    }
}
