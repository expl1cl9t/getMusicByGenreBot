using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Threading;
using System.Diagnostics;

namespace ConfiguratorToParser
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<string>? genres_main_list;
        public MainWindow()
        {
            InitializeComponent();
        }
        public void addGenreButton(object sender, RoutedEventArgs e)
        {
            Random r = new Random();
            Color[] colors = new Color[] {Colors.Gold, Colors.IndianRed,Colors.Honeydew};
            ComboBox genre = new ComboBox();
            genre.SelectedItem = "Метал";
            genre.Items.Add("Метал");
            genre.Items.Add("Рэп");
            genre.Background = new SolidColorBrush(colors[r.Next(0,colors.Length - 1)]);
            genre.FontSize = 20;
            //genre.SelectionChanged += addToList;
            genres.Children.Add(genre);
        }

        private void IsNeedToAddAccounts(object sender, RoutedEventArgs e)
        {
                accounts.IsEnabled = true;
        }

        private void SaveConfigurationButton(object sender, RoutedEventArgs e)
        {
            string? genre = genre_selector.Text.ToString();
            bool? isEnableAccs = addAccountsOrNot.IsChecked;
            bool? schedudled = Schedudler.IsChecked;
            Account acc;
            if(isEnableAccs == true)
            {
                acc = new Account();
                acc.Type = TypeOfAccount.Text;
                acc.Name = NameOfAccount.Text;
            }
            else
            {
                acc = new Account();
                acc.Type = "null";
                acc.Name = "null";
            }
            var config = new Properties
            {
                Account = acc,
                isEnableBroadcastToAccounts = isEnableAccs,
                isEnadbleSchedudler = schedudled,
                Genre = genre,
                NameOfLastAlbum = ""
            };
            string filename = "configuration.json";
            string parsed = JsonSerializer.Serialize(config);
            File.WriteAllText(filename,parsed);
            Process.Start("CMD.EXE","/c py main.py");
            MessageBox.Show($"Файл конфигурации сохранён в {filename}");
            }
        }
    }
