<template>
    <el-container style="border: 1px solid #eee">
        <el-container>
            <el-main>
                <div ref="charts" style="width: 100%; height: 100vh"></div>
            </el-main>
        </el-container>

        <el-dialog title="Data Sources" :visible.sync="dialogVisible" width="60%" :before-close="handleClose">
            <div v-for="(item, inds) in linksData.links" :key="inds">{{ `${item.date}  ` }} <el-link type="primary"
                    :href="item.link">{{ item.name }}</el-link> </div>
            <span slot="footer" class="dialog-footer">
                <el-button size="small" type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </el-dialog>
    </el-container>
</template>
<style scoped lang="scss">
$main-color: #f1f5fb;

* {
    font-size: 1.6rem;
}

body>.el-container {
    margin-bottom: 40px;
}

.el-main,
.el-container {
    background-color: $main-color;
}

.el-container {
    overflow-x: auto;
    min-width: 1200px;
    height: 100vh;
}

.el-main {
    background-color: #FFF;
    color: #333;
    text-align: center;
    overflow: visible;
}
</style>
<script>
import usaJson from "@/assets/USA.json"

export default {
    data() {
        return {
            dataSet: {
                resultdata1: [
                    { name: 'Alabama', value: 2 },
                    { name: 'Alaska', value: 1 },
                    { name: 'Arizona', value: 0 },
                    { name: 'Arkansas', value: 0 },
                    { name: 'California', value: 7 },
                    { name: 'Colorado', value: 1 },
                    { name: 'Connecticut', value: 0 },
                    { name: 'Delaware', value: 0 },
                    { name: 'District of Columbia', value: 0 },
                    { name: 'Florida', value: 4 },
                    { name: 'Georgia', value: 0 },
                    { name: 'Hawaii', value: 0 },
                    { name: 'Idaho', value: 0 },
                    { name: 'Illinois', value: 0 },
                    { name: 'Indiana', value: 0 },
                    { name: 'Iowa', value: 0 },
                    { name: 'Kansas', value: 2 },
                    { name: 'Kentucky', value: 0 },
                    { name: 'Louisiana', value: 0 },
                    { name: 'Maine', value: 0 },
                    { name: 'Maryland', value: 0 },
                    { name: 'Massachusetts', value: 0 },
                    { name: 'Michigan', value: 1 },
                    { name: 'Minnesota', value: 2 },
                    { name: 'Mississippi', value: 1 },
                    { name: 'Missouri', value: 0 },
                    { name: 'Montana', value: 0 },
                    { name: 'Nebraska', value: 0 },
                    { name: 'Nevada', value: 0 },
                    { name: 'New Hampshire', value: 0 },
                    { name: 'New Jersey', value: 0 },
                    { name: 'New Mexico', value: 0 },
                    { name: 'New York', value: 1 },
                    { name: 'North Carolina', value: 0 },
                    { name: 'North Dakota', value: 0 },
                    { name: 'Ohio', value: 0 },
                    { name: 'Oklahoma', value: 2 },
                    { name: 'Oregon', value: 4 },
                    { name: 'Pennsylvania', value: 1 },
                    { name: 'Rhode Island', value: 0 },
                    { name: 'South Carolina', value: 0 },
                    { name: 'South Dakota', value: 0 },
                    { name: 'Tennessee', value: 1 },
                    { name: 'Texas', value: 4 },
                    { name: 'Utah', value: 0 },
                    { name: 'Vermont', value: 0 },
                    { name: 'Virginia', value: 0 },
                    { name: 'Washington', value: 6 },
                    { name: 'West Virginia', value: 0 },
                    { name: 'Wisconsin', value: 0 },
                    { name: 'Wyoming', value: 0 },
                    { name: 'Puerto Rico', value: 0 }
                ],
                resultdata2: [
                    { name: 'Alabama', value: 1 },
                    { name: 'Alaska', value: 1 },
                    { name: 'Arizona', value: 0 },
                    { name: 'Arkansas', value: 0 },
                    { name: 'California', value: 9 },
                    { name: 'Colorado', value: 1 },
                    { name: 'Connecticut', value: 0 },
                    { name: 'Delaware', value: 0 },
                    { name: 'District of Columbia', value: 0 },
                    { name: 'Florida', value: 6 },
                    { name: 'Georgia', value: 0 },
                    { name: 'Hawaii', value: 0 },
                    { name: 'Idaho', value: 1 },
                    { name: 'Illinois', value: 0 },
                    { name: 'Indiana', value: 0 },
                    { name: 'Iowa', value: 0 },
                    { name: 'Kansas', value: 2 },
                    { name: 'Kentucky', value: 0 },
                    { name: 'Louisiana', value: 0 },
                    { name: 'Maine', value: 0 },
                    { name: 'Maryland', value: 0 },
                    { name: 'Massachusetts', value: 1 },
                    { name: 'Michigan', value: 1 },
                    { name: 'Minnesota', value: 1 },
                    { name: 'Mississippi', value: 1 },
                    { name: 'Missouri', value: 0 },
                    { name: 'Montana', value: 0 },
                    { name: 'Nebraska', value: 0 },
                    { name: 'Nevada', value: 0 },
                    { name: 'New Hampshire', value: 0 },
                    { name: 'New Jersey', value: 0 },
                    { name: 'New Mexico', value: 0 },
                    { name: 'New York', value: 1 },
                    { name: 'North Carolina', value: 0 },
                    { name: 'North Dakota', value: 0 },
                    { name: 'Ohio', value: 0 },
                    { name: 'Oklahoma', value: 2 },
                    { name: 'Oregon', value: 1 },
                    { name: 'Pennsylvania', value: 1 },
                    { name: 'Rhode Island', value: 0 },
                    { name: 'South Carolina', value: 0 },
                    { name: 'South Dakota', value: 0 },
                    { name: 'Tennessee', value: 1 },
                    { name: 'Texas', value: 3 },
                    { name: 'Utah', value: 0 },
                    { name: 'Vermont', value: 0 },
                    { name: 'Virginia', value: 0 },
                    { name: 'Washington', value: 4 },
                    { name: 'West Virginia', value: 0 },
                    { name: 'Wisconsin', value: 0 },
                    { name: 'Wyoming', value: 0 },
                    { name: 'Puerto Rico', value: 0 }
                ]
            },
            linksData: {},
            dialogVisible: false,
        stateLinks: {
                'Alabama': [
                    {
                        date: '',
                        name: 'Could an Alabama woman have shot herself twice?',
                        link: 'https://www.cbsnews.com/pictures/tiffiney-crawford-cullman-alabama-death-investigation-photos/'
                    },
                ],
                'Alaska': [
                    {
                        date: '',
                        name: '"People are suffering": Food stamp woes worsen Alaska hunger',
                        link: 'https://abcnews.go.com/Health/wireStory/people-suffering-food-stamp-woes-worsen-alaska-hunger-98785300'
                    },
                ],
                'Michigan': [
                    {
                        date: '',
                        name: 'Fungal outbreak at Michigan paper mill suspected to have infected nearly 100 workers',
                        link: 'https://www.nbcnews.com/news/us-news/fungal-outbreak-michigan-paper-mill-suspected-infected-nearly-100-work-rcna79159'
                    },
                    {
                        date: '',
                        name: 'One death and almost 100 cases of rare fungal infection linked to Michigan paper mill, health officials say',
                        link: 'https://www.cnn.com'
                    },
                ],
                'Texas': [
                    {
                        date: '',
                        name: 'What is mifepristone, the drug at the heart of the Texas medication abortion lawsuit?',
                        link: 'https://www.cnn.com/2023/03/15/health/mifepristone-what-is-it/index.html'
                    },
                    {
                        date: '',
                        name: 'Bill to combat youth fentanyl crisis to be introduced after multiple teens overdose in a Texas school district',
                        link: 'https://www.nbcnews.com/news/proposed-bill-aimed-combatting-youth-fentanyl-crisis-rcna80883'
                    },
                    {
                        date: '',
                        name: 'Texas lawmaker slams school safety bills without gun restrictions',
                        link: 'https://www.nbcnews.com/news/latino/texas-democrat-lawmaker-slams-school-safety-bills-no-gun-restrictions-rcna81381'
                    },
                ],
                'Florida': [
                    {
                        date: '',
                        name: '1. Florida surgeon general altered Covid-19 vaccine analysis to suggest higher risk for younger men, Politico reports',
                        link: 'https://www.cnn.com/2023/04/25/health/florida-covid-vaccine-analysis-ladapo/index.html'
                    },
                    {
                        date: '',
                        name: '2. Florida GOP files proposal clearing the way for a DeSantis 2024 bid',
                        link: 'https://www.nbcnews.com/politics/2024-election/florida-gop-files-proposal-clear-way-ron-desantis-2024-rcna81416'
                    },
                    {
                        date: '',
                        name: '3. How a 2019 Florida law catalyzed a hospital-building boom',
                        link: 'https://www.usatoday.com/story/news/health/2023/04/22/florida-hospital-building-boon/11696095002/'
                    },
                    {
                        date: '',
                        name: '4. Florida Gov. Ron DeSantis expansion of so-called “Dont Say Gay” law approved by state board',
                        link: 'https://abcnews.go.com/Health/wireStory/florida-gov-ron-desantis-expansion-called-dont-gay-98697723'
                    },
                    {
                        date: '',
                        name: '5. Suspect in "killer clown" case pleads guilty in 1990 murder of Florida woman.Sheila Keen-Warren is accused of dressing up as clown in 1990 and fatally shooting the wife of a man she later married',
                        link: 'https://www.cbsnews.com/news/sheila-keen-warren-killer-clown-case-pleads-guilty-marlene-warren-1990-murder/'
                    },
                    {
                        date: '',
                        name: "6. Alisa Mathewson 55 hours of terror.Evidence photos depict the Florida mother's ordeal after her estranged husband snuck into her home and proceeded to hold her against her will.",
                        link: 'https://www.cbsnews.com/pictures/alisa-mathewson-trevor-summers-55-hours-of-terror/'
                    },
                ],
                'New York': [
                    {
                        date: '',
                        name: '© 2023 The New York Times Company',
                        link: 'https://help.nytimes.com/hc/en-us/articles/115014792127-Copyright-notice'
                    },
                ],
                'California': [
                    {
                        date: '',
                        name: '1. California mother sentenced to life for murder and torture of 10-year-old son Anthony Avalos',
                        link: 'https://www.nbcnews.com/news/us-news/mother-sentenced-murder-torture-10-year-old-son-rcna81387'
                    },
                    {
                        date: '',
                        name: '2. Will record numbers of mosquitoes follow record California rains?',
                        link: 'https://www.usatoday.com/story/news/nation/2023/04/14/more-mosquitoes-california-summer/11648419002/'
                    },
                    {
                        date: '',
                        name: '3. Your California Privacy Rights / Privacy Policy',
                        link: 'https://cm.usatoday.com/privacy-policy'
                    },
                    {
                        date: '',
                        name: '4. California fake "doctor" treated thousands, including cancer patients, prosecutors say',
                        link: 'https://www.cbsnews.com/news/los-angeles-fake-doctor-stephan-gevorkian-practicing-medicine-without-license/'
                    },
                    {
                        date: '',
                        name: '5. California considers ban on 5 food additives linked to health risks',
                        link: 'https://www.cbsnews.com/news/food-additives-health-risks-banned-california/'
                    },
                    {
                        date: '',
                        name: '6. California considers ban on 5 food additives linked to health risks',
                        link: 'https://www.cbsnews.com/news/food-additives-health-risks-banned-california/'
                    },
                    {
                        date: '',
                        name: '7. California fake "doctor" treated thousands, including cancer patients, prosecutors say Prosecutors charged 43-year-old Stephan Gevorkian with five felony counts of practicing medicine without a certification, according to District Attorney George Gascón.',
                        link: 'https://www.cbsnews.com/news/los-angeles-fake-doctor-stephan-gevorkian-practicing-medicine-without-license/'
                    },
                    {
                        date: '',
                        name: "8. California man who impersonated a doctor practiced on 'thousands of individuals,' Los Angeles DA says",
                        link: 'https://www.foxnews.com/us/california-man-who-impersonated-doctor-practiced-thousands-individuals-los-angeles-da-says'
                    },
                    {
                        date: '',
                        name: '9. Stephan Gevorkian of Studio City, California, is facing charges after the Los Angeles County District Attorney’s Office says he falsely claimed to be a licensed doctor.',
                        link: 'https://www.foxnews.com/us/california-man-who-impersonated-doctor-practiced-thousands-individuals-los-angeles-da-says'
                    },
                ],
                'Washington': [
                    {
                        date: '',
                        name: '1. Washington Post Live',
                        link: 'https://www.washingtonpost.com/washington-post-live/'
                    },
                    {
                        date: '',
                        name: '2. New Washington gun law already faces federal court challenge',
                        link: 'https://abcnews.go.com/Health/wireStory/gov-inslee-signs-washington-gun-violence-prevention-bills-98837864'
                    },
                    {
                        date: '',
                        name: '3. New Washington gun law already faces federal court challenge',
                        link: 'https://abcnews.go.com/Health/wireStory/gov-inslee-signs-washington-gun-violence-prevention-bills-98837864'
                    },
                    {
                        date: '',
                        name: '4. Ban on many semi-automatic rifles passes Washington state Legislature as mass shootings soar; governor expected to sign',
                        link: 'https://abcnews.go.com/Health/wireStory/ban-semi-automatic-rifles-passes-washington-state-legislature-98709029'
                    },
                ],
                'Colorado': [
                    {
                        date: '',
                        name: "Colorado says it won't enforce 'abortion reversal' ban",
                        link: 'https://abcnews.go.com/Health/wireStory/colorado-enforce-abortion-reversal-ban-98764223'
                    },
                ],
                'Oregon': [
                    {
                        date: '',
                        name: 'Oregon secures 3-year supply of abortion-inducing medication',
                        link: 'https://abcnews.go.com/Health/wireStory/oregon-secures-3-year-supply-abortion-inducing-medication-98742975'
                    },
                ],
                'Kansas': [
                    {
                        date: '',
                        name: 'Kansas governor vetoes 4 anti-trans bills as overrides loom',
                        link: 'https://abcnews.go.com/Health/wireStory/kansas-governor-vetoes-bills-trans-youth-care-bathrooms-98738057'
                    },
                    {
                        date: '',
                        name: 'Kansas governor vetoes bills restricting bathrooms for transgender people and gender-affirming care for minors',
                        link: 'https://abcnews.go.com/Health/wireStory/kansas-governor-vetoes-bills-restricting-bathrooms-transgender-people-98738050'
                    },
                ],
                'Mississippi': [
                    {
                        date: '',
                        name: "Mississippi governor touts 'culture of life' with new laws",
                        link: 'https://abcnews.go.com/Health/wireStory/mississippi-governor-touts-culture-life-new-laws-98705913e'
                    },
                ],
                'Minnesota': [
                    {
                        date: '',
                        name: "In Minnesota's worst measles outbreak, a battle of beliefs over vaccines",
                        link: 'https://abcnews.go.com/Health/minnesotas-worst-measles-outbreak-battle-beliefs-vaccines/story?id=47155531 '
                    },
                ],
                'Idaho': [
                    {
                        date: '',
                        name: 'Surviving roommate in Idaho student murders fights subpoena to appear at hearing',
                        link: 'https://www.cbsnews.com/news/idaho-student-murders-bryan-kohberger-hearing-surviving-roommate-fights-subpeona/'
                    },
                ],
                'Pennsylvania': [
                    {
                        date: '',
                        name: "Pennsylvania hospital shutdown strains area's health care system",
                        link: 'https://www.cbsnews.com/news/pennsylvania-hospital-shutdown-strains-health-care-delivery-first-responders-say/'
                    },
                ],
                'Massachusetts': [
                    {
                        date: '',
                        name: 'Massachusetts',
                        link: 'https://www.foxnews.com/category/us/us-regions/northeast/massachusetts'
                    },
                ],



            },
    }},
    methods: {
        initCharts() {
        const myCharts = this.$echarts.init(this.$refs["charts"]);
        const { resultdata1, resultdata2 } = this.dataSet;
        resultdata1.forEach(item => {
            const stateName = item.name;
            item.links = this.stateLinks[stateName] || [];
        });
        resultdata2.forEach(item => {
            const stateName = item.name;
            item.links = this.stateLinks[stateName] || [];
        });
        const option = {
                title: [{
                    text: 'EpidemicMediaInsight',
                    sublink: 'http://www.census.gov/popest/data/datasets.html',
                    left: 'left',
                    textStyle:{
                        fontSize: 30
                    }
                }
                    // ,{
                    //     text: '',
                    //     sublink: 'http://www.census.gov/popest/data/datasets.html',
                    //     left: 'right'
                    // }
                ],
                legend: {
                    data: ['Social Media', 'Traditional Press'],
                    top: '5%',
                    left: '40%',
                    selectedMode: 'single',
                    selected: {
                        'Social Media': true,
                        'Traditional Press': false
                    },
                    textStyle: {
                        fontSize: '22'
                    }
                },
                tooltip: {
                    trigger: 'item',
                    showDelay: 0,
                    transitionDuration: 0.2
                },
                visualMap: {
                    right: '8%',
                    bottom: '10%',
                    min: 0,
                    max: 7,
                    inRange: {
                        color: [
                            '#FFFFFF',
                            '#4575b4',
                            '#74add1',
                            '#abd9e9',
                            '#e0f3f8',
                            '#ffffbf',
                            '#fee090',
                            '#fdae61',
                            '#f46d43',
                            '#d73027',
                            '#a50026'
                        ]
                    },
                    text: ['High', 'Low'],
                    calculable: true
                },
                series: [
                    {
                        name: 'Social Media',
                        type: 'map',
                        roam: true,
                        top: 'middle',
                        scaleLimit: {
                            min: 1,
                            max: 2.6
                        },
                        map: 'USA',
                        label: {
                            normal: {
                                show: true,
                            },
                            emphasis: {
                                show: true,
                            },
                        },
                        emphasis: {
                            label: {
                                show: true
                            }
                        },
                        data: resultdata1
                    },
                    {
                        name: 'Traditional Press',
                        type: 'map',
                        roam: true,
                        top: 'middle',
                        scaleLimit: {
                            min: 1,
                            max: 2.6
                        },
                        map: 'USA',
                        label: {
                            normal: {
                                show: true,
                            },
                            emphasis: {
                                show: true,
                            },
                        },
                        emphasis: {
                            label: {
                                show: true
                            }
                        },
                        data: resultdata2
                    }
                ]
            };

            console.log('ass', typeof usaJson)
            usaJson.features.forEach(item => {
                item.properties.name = item.properties.name_full
            })
            // Map registration, the name of the first parameter must be consistent with option.geo.map
            this.$echarts.registerMap('USA', usaJson, {
                Alaska: {
                    left: -131,
                    top: 25,
                    width: 15
                },
                Hawaii: {
                    left: -110,
                    top: 28,
                    width: 5
                },
                'Puerto Rico': {
                    left: -76,
                    top: 26,
                    width: 2
                }
            });

            myCharts.setOption(option);
            myCharts.on("click", params => { //click event
                console.log('I was clicked', params)
                this.clickItem(params)
            });
        },
        //Click on the event for each state
        clickItem(params) {
            this.linksData = params.data
            this.dialogVisible = true
        },
        handleClose() {
            this.dialogVisible = false
        }
    },
    mounted() {
        this.initCharts();
    }
}
</script>
  